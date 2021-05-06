#!/usr/bin/env python3
## Author: lehag
## Code: T1518-001-AVDiscovery.py
"""
	Description:
		It discovers if an antivirus is active.
"""
import subprocess
import sys

if __name__ == "__main__":
	print("[+] Discovering antivirus on the system.");

	## Discovers antivirus on the system
	result = subprocess.run(["wmic", "/namespace:\\\\root\\securitycenter2", "path", "antivirusproduct"]);
  
