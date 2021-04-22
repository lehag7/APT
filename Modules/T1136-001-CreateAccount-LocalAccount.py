## Author: lehag
## Code: T1136-001-CreateAccount-LocalAccount.py
"""
	Description:
		It creates a local account.
"""
import subprocess
import sys

if __name__ == "__main__":
	print("[+] Creating a local account.");

	## Creates a local account.
	result = subprocess.run(["net", "user", "Fulanito", "abc123", "/add"]);
