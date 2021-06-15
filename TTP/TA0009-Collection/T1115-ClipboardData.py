#!/usr/bin/env python3
## Author: lehag
## Code: T1115-ClipboardData.py
"""
	Description:
		It collects data stored in the clipboard.
"""
import win32clipboard

if __name__ == "__main__":
	print("[+] Collecting data stored in the clipboard.");

	## Collects data stored in the clipboard.
	win32clipboard.OpenClipboard(0);
	result = win32clipboard.GetClipboardData();
	print(result);
