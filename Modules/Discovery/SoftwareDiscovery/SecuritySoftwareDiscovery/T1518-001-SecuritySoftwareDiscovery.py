#!/usr/bin/env python3
## Author: lehag
## Code: T1518-001-SecuritySoftwareDiscovery.py
"""
	Description:
		It discovers if an antivirus is active.        
"""
import subprocess
import sys

def executeSSDViaWMIC():
    ## Discovers antivirus on the system via WMIC
    result = subprocess.run(["wmic.exe", "/namespace:\\\\root\\securitycenter2", "path", "antivirusproduct"]);
    return;

def executeSSDViaPowershell():
    ## Discovers antivirus on the system via Powershell
    command = ["powershell.exe", "Get-CimInstance", "-Namespace", "root/SecurityCenter2", "-ClassName", "AntivirusProduct"];
    result = subprocess.run(command);
    return;

def executeSSDViaRegister():
    ## Discovers antivirus on the system via Register
    command = ["reg.exe", "query", "HKLM\\SOFTWARE\\Microsoft\\Security Center\\Provider\\Av", "/s"];
    result = subprocess.run(command);
    return;

def executeSSDViaAPI():
    ## Discovers antivirus on the system via API
    return;

if __name__ == "__main__":
    while(True):
        print("[+] Security Software Discovery");
        print("\t1. Via Wmic");
        print("\t2. Via Powershell");
        print("\t3. Via Register");
        print("\t4. Via API");
        print("\t5. Exit");
        opcion = int(input("\t[>] Select the Procedure to test: "));

        if(opcion == 1):
            executeSSDViaWMIC();
            continue;
        elif(opcion == 2):
            executeSSDViaPowershell();
            continue;
        elif(opcion == 3):
            executeSSDViaRegister();
            continue;
        elif(opcion == 4):
            executeSSDViaAPI();
            continue;
        elif(opcion == 5):
            exit(0);
        else:
            print("[-] Invalid option.");

  
