import hashlib
import json
import os
import time

def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def monitor_files():
    with open("hashes.json", "r") as f:
        baseline_hashes = json.load(f)

    for file, old_hash in baseline_hashes.items():
        if not os.path.exists(file):
            print(f"⚠️ WARNING: File missing -> {file}")
            continue

        current_hash = calculate_hash(file)

        if current_hash != old_hash:
            print(f" ALERT: Unauthorized modification detected -> {file}")
        else:
            print(f" SAFE: No change -> {file}")

if __name__ == "__main__":
    print("Starting file integrity monitoring...\n")
    while True:
        monitor_files()
        print("-" * 40)
        time.sleep(30)  # Scan every 30 seconds
