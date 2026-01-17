import hashlib
import json
import os

FILES_TO_MONITOR = [
    "files/sample.txt",
    "files/config.env",
    "files/app.conf"
]

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def create_baseline():
    hashes = {}

    for file in FILES_TO_MONITOR:
        if os.path.exists(file):
            hashes[file] = calculate_hash(file)
        else:
            print(f"[WARNING] File not found: {file}")

    with open("hashes.json", "w") as f:
        json.dump(hashes, f, indent=4)

    print("Baseline hashes successfully created.")

if __name__ == "__main__":
    create_baseline()
