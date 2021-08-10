#!/usr/bin/env python3
## Author: lehag
## Code: T1057-ProcessDiscovery.py
"""
	Description:
		It lists all the active processes.
"""
from ctypes import *
from ctypes.wintypes import *

# Establish rights and basic options needed for all process declaration/iteration.
TH32CS_SNAPPROCESS = 0x02;
STANDARD_RIGHTS_REQUIRED = 0x000F0000;
SYNCHRONIZE = 0x00100000;
PROCESS_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0xFFF);
TH32CS_SNAPMODULE = 0x00000008;
TH32CS_SNAPTHREAD = 0x00000004;
INVALID_HANDLE_VALUE = -1;

##  Create object definitions to store information in them
""" ## 32 bits
class PROCESSENTRY32(Structure):
    _fields_ = [('dwSize', c_uint),
                ('cntUsage', c_uint),
                ('th32ProcessID', c_uint),
                ('th32DefaultHeapID', c_uint),
                ('th32ModuleID', c_uint),
                ('cntThreads', c_uint),
                ('th32ParentProcessID', c_uint),
                ('pcPriClassBase', c_long),
                ('dwFlags', c_uint),
                ('szExeFile', c_char * 260)]
"""
## 64 bits
class PROCESSENTRY32(Structure):
    _fields_ = [('dwSize', DWORD),
                ('cntUsage', DWORD),
                ('th32ProcessID', DWORD),
                ('th32DefaultHeapID', POINTER(ULONG)),
                ('th32ModuleID', DWORD) ,
                ('cntThreads', DWORD) ,
                ('th32ParentProcessID', DWORD),
                ('pcPriClassBase', LONG),
                ('dwFlags', DWORD) ,
                ('szExeFile', c_char * 260)];

if __name__ == "__main__":
    ## Get functions from windll.kernel32. General declarations.
    CreateToolhelp32Snapshot = windll.kernel32.CreateToolhelp32Snapshot;
    Process32First = windll.kernel32.Process32First;
    Process32Next = windll.kernel32.Process32Next;
    GetLastError = windll.kernel32.GetLastError;
    OpenProcess = windll.kernel32.OpenProcess;
    GetPriorityClass = windll.kernel32.GetPriorityClass;
    CloseHandle = windll.kernel32.CloseHandle;

    ## Lists all the active processes.
    print("[+] Listing all the active processes.");
    try:
        hProcessSnap = c_void_p(0);
        pe32 = PROCESSENTRY32();  ## Declare class/structure

        ## Take a snapshot of all processes in the system.
        hProcessSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
        if(hProcessSnap == INVALID_HANDLE_VALUE):
            print("[-] CreateToolhelp32Snapshot ERROR");
            exit(0);

        ## Set the size of the structure before using it.
        pe32.dwSize = sizeof(PROCESSENTRY32);

        ## Retrieve information about the first process, and exit if unsuccessful.
        ret = Process32First(hProcessSnap, pointer(pe32));
        if(not ret):
            print("[-] Process32First ERROR");
            CloseHandle(hProcessSnap);
            exit(0);

        ## Now walk the snapshot of processes, and display information about each process in turn
        print("Process\tPID\tThread count\tPPID");
        print("============================================================");

        while(True):
            ## Print process information
            hProcess = OpenProcess(PROCESS_ALL_ACCESS, 0, pe32.th32ProcessID);
        
            dwPriorityClass = GetPriorityClass(hProcess);
            if(dwPriorityClass == 0):
                CloseHandle(hProcess);

            print(pe32.szExeFile.decode() + "\t" + str(pe32.th32ProcessID) + "\t" + str(pe32.cntThreads) + "\t" + str(pe32.th32ParentProcessID));
            ##if(dwPriorityClass):
            ##    print(dwPriorityClass);

            if(Process32Next(hProcessSnap, pointer(pe32))):
                continue;
            else:
                break;
        CloseHandle (hProcessSnap);
    except:
        print("[-] Error listing all the active processes.");
