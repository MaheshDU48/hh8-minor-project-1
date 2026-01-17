# Tamper Detection – File Integrity Monitor

# Project Description
This project monitors file integrity by generating cryptographic hashes and detecting unauthorized changes in critical files.

# Tools Used
- Python
- Hashlib
- JSON
- OS module

# How to Run
1. Create baseline hashes:
   python baseline.py

2. Start monitoring:
   python monitor.py

# How It Works
- Baseline hashes are generated using SHA-256
- Current file hashes are compared periodically
- Alerts are raised if changes are detected

# What I Learned
- File integrity monitoring concepts
- Cryptographic hashing
- Secure file comparison
- Python file handling

# Tips
- Monitor .env and configuration files
- Store baseline hashes securely
- Run integrity checks periodically

baseline.py run:
command-python baseline.py
![Image](https://github.com/user-attachments/assets/cba516b3-c27b-4481-b84c-496ce530bcf6)

monitor.py run
![Image](https://github.com/user-attachments/assets/a453c4ac-e821-408c-a6cd-1a8e786adf15)
