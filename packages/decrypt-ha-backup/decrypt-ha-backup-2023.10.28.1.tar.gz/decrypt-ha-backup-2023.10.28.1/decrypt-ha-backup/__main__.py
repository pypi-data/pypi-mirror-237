import argparse
from io import BytesIO
import string
import sys
import hashlib
import tarfile
import json
import os
import random
import getpass
from typing import IO
import tempfile
import platform
from pathlib import Path
from .hacked_secure_tar_file import HackedSecureTarFile

class FailureError(Exception):
    """Indicates a failure with a user readable message attached"""
    
    def __init__(self, message: str) -> None:
        """Initialize failure error."""
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        """Return string representation of failure error."""
        return self.message


def password_to_key(password: str) -> bytes:
    """Generate a AES Key from password."""
    key: bytes = password.encode("utf-8")
    for _ in range(100):
        key = hashlib.sha256(key).digest()
    return key[:16]

def key_to_iv(key: bytes) -> bytes:
    """Generate an iv from Key."""
    for _ in range(100):
        key = hashlib.sha256(key).digest()
    return key[:16]

def overwrite(line: str):
    sys.stdout.write(f"\r{line.encode('utf-8', 'replace').decode()}\033[K")

def readTarMembers(tar: tarfile.TarFile):
    while(True):
        member = tar.next()
        if member is None:
            break
        else:
            yield member

class Backup:
    def __init__(self, tarfile: tarfile.TarFile):
        self._tarfile = tarfile
        try:
            self._configMember = self._tarfile.getmember("./snapshot.json")
        except KeyError:
            self._configMember = self._tarfile.getmember("./backup.json")
        json_file = self._tarfile.extractfile(self._configMember)
        if not json_file:
            raise FailureError("Backup doesn't contain a metadata file named 'snapshot.json' or 'backup.json'")
        self._config = json.loads(json_file.read())
        json_file.close()
        self._items = [BackupItem(entry['slug'], entry['name'], self) for entry in self._config.get("addons")]
        self._items += [BackupItem(entry, self.folderSlugToName(entry), self) for entry in self._config.get("folders")]

        if self._config.get('homeassistant') is not None:
            self._items.append(BackupItem('homeassistant', self.folderSlugToName('homeassistant'), self)) 


    def folderSlugToName(self, slug):
        if slug == "homeassistant":
            return "Config Folder"
        elif slug == "addons/local":
            return "Local Add-ons"
        elif slug == "media":
            return "Media Folder"
        elif slug == "share":
            return "Share Folder"
        elif slug == "ssl":
            return "SSL Folder"
        else:
            return slug

    @property
    def compressed(self):
        return self._config.get("compressed", True)

    @property
    def encrypted(self):
        return self._config.get('protected', False)

    @property
    def items(self):
        return self._items

    @property
    def version(self):
        return self._config.get('version')

    def create_slug(self) -> str:
        key = ''.join(random.choice(string.ascii_uppercase) for _ in range(50)).encode()
        return hashlib.sha1(key).hexdigest()[:8]

    def addModifiedConfig(self, tarfile: tarfile.TarFile):
        clear = self._config.copy()
        clear['crypto'] = None
        clear['protected'] = False
        clear['slug'] = self.create_slug()
        clear['name'] = "Decrypted " + clear['name']
        bytes = json.dumps(clear, indent=2).encode('utf-8')
        file = BytesIO(bytes)
        self._configMember.size = len(bytes)
        tarfile.addfile(self._configMember, file)


class BackupItem:
    def __init__(self, slug, name, backup: Backup):
        self._slug = slug
        self._name = name
        self._backup = backup
        self._info = self._backup._tarfile.getmember(self.fileName)
        if not self._info:
            raise FailureError(f"Backup file doesn't contain a file for {self._name} with the name '{self.fileName}'")

    @property
    def fileName(self):
        ext = ".tar.gz" if self._backup.compressed else ".tar"
        return f"./{self._slug.replace('/', '_')}{ext}"

    @property
    def slug(self):
        return self._slug

    @property
    def name(self):
        return self._name

    @property
    def info(self) -> tarfile.TarInfo:
        return self._info

    @property
    def size(self):
        return self.info.size

    def _open(self):
        data = self._backup._tarfile.extractfile(self.info)
        if not data:
            raise FailureError(f"Backup file doesn't contain a file named {self.info.name}")
        return data

    def _extractTo(self, file: IO):
        progress = 0
        encrypted = self._open()
        overwrite(f"Extracting '{self.name}' 0%")
        while(True):
            data = encrypted.read(1024 * 1024)
            if len(data) == 0:
                break
            file.write(data)
            overwrite(f"Extracting '{self.name}' {round(100 * progress/self.size, 1)}%")
            progress += len(data)
        overwrite(f"Extracting '{self.name}' {round(100 * progress/self.size, 1)}%")
        print()

    def _copyTar(self, source: tarfile.TarFile, dest: tarfile.TarFile):
        for member in readTarMembers(source):
            overwrite(f"Decrypting '{self.name}' file '{member.name}'")
            if not tarfile.TarInfo.isreg(member):
                dest.addfile(member)
            else:
                dest.addfile(member, source.extractfile(member))

    def addTo(self, temp_folder: str, output: tarfile.TarFile, key: bytes):
        temp_file = os.path.join(temp_folder, os.urandom(24).hex())
        try:
            with open(temp_file, "wb") as f:
                self._extractTo(f)
            overwrite(f"Decrypting '{self.name}'")
            with HackedSecureTarFile(Path(temp_file), key=key, gzip=self._backup.compressed) as decrypted:
                with tempfile.NamedTemporaryFile() as processed:
                    tarmode = "w|" + ("gz" if self._backup.compressed else "")
                    with tarfile.open(f"{self.slug}.tar", tarmode, fileobj=processed) as archivetar:
                        self._copyTar(decrypted, archivetar)
                    processed.flush()
                    overwrite(f"Decrypting '{self.name}' done")
                    print()
                    info = self.info
                    info.size = os.stat(processed.name).st_size
                    processed.seek(0)
                    overwrite(f"Saving '{self.name}' ...")
                    output.addfile(info, processed)
                    overwrite(f"Saving '{self.name}' done")
                    print()
        finally:
            if os.path.isfile(temp_file):
                os.remove(temp_file)
            pass


def main():
    parser = argparse.ArgumentParser(description="Decrypts an encrypted Home Assistant backup file", prog="decrypt_ha_backup")
    parser.add_argument("backup_file", help='The backup file that should be decrypted')
    parser.add_argument("--output_file", "-o", help='The name of decrypted backup file to be created.  If not specified, it will be chosen based on the backup name.')
    parser.add_argument("--password", "-p", "--pass", help="The password for the backup.  If not specified, you will be prompted for it.")
    args = parser.parse_args()

    if not os.path.exists(args.backup_file):
        print("The specified backup file couldn't be found")
        exit()

    if args.output_file is None:
        parts = list(Path(args.backup_file).parts)
        parts[-1] = "Decrypted " + parts[-1]
        args.output_file = os.path.join(*parts)

    if os.path.exists(args.output_file):
        resp = input(f"The output file '{args.output_file}' already exists, do you want to overwrite it [y/n]?")
        if not resp.startswith("y"):
            print("Aborted")
            exit(1)

    if args.password is None:
        # ask fro a password
        args.password = getpass.getpass("Backup Password:")

    temp_dir = tempfile.gettempdir()
    try:
        with tarfile.open(Path(args.backup_file), "r:") as backup_file:
            backup = Backup(backup_file)
            if not backup.encrypted:
                print("This backup file isn't encrypted")
                return
            if backup.version != 2:
                print(f"Only backup format 'Version 2' is supported, this backup is 'Version {backup.version}'")
                return

            _key = password_to_key(args.password)
            print(_key)

            with tarfile.open(args.output_file, "w:") as output:
                for archive in backup.items:
                    archive.addTo(temp_dir, output, _key)

                # Add the modified backup config
                backup.addModifiedConfig(output)

        print(f"Created backup file '{args.backup_file}'")
    except tarfile.ReadError as e:
        if "not a gzip file" in str(e):
            print("The file could not be read as a gzip file.  Please ensure your password is correct.")
        else:
            raise
    except FailureError as e:
        print(e)
        exit(1)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        from ctypes import windll
        windll.kernel32.SetConsoleMode(windll.kernel32.GetStdHandle(-11), 7)
    main()