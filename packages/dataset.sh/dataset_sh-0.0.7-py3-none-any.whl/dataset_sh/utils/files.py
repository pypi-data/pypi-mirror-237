import hashlib
import os


def checksum(file_path):
    md5_hash = hashlib.md5()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            md5_hash.update(data)

    return md5_hash.hexdigest()


def filesize(file_path):
    file_size = os.path.getsize(file_path)
    return file_size
