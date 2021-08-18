#!/usr/bin/env python3
## Author: lehag
## Code: APT.py
"""
    Description:
        This project (WIP) aims to be a framework composed of modules that allow blue teams to test their threat detection capabilities in their environments by emulating the Tactics, Techniques and Procedures (TTP) followed by an adversary based on MITRE ATT&CK.
"""
import json
import subprocess
import sys

class APT:
    if __name__ == "__main__":
        print("""
                 █████╗    ██████╗ ████████╗
                ██╔══██╗   ██╔══██╗╚══██╔══╝
                ███████║   ██████╔╝   ██║   
                ██╔══██║   ██╔═══╝    ██║   
                ██║  ██║██╗██║██╗     ██║   
                ╚═╝  ╚═╝╚═╝╚═╝╚═╝     ╚═╝   : Advanced Persistence Testing.
        """);
        print("[+] Description: This project (WIP) aims to be a framework composed of modules that allow blue teams to test their threat detection capabilities in their environments by emulating the Tactics, Techniques and Procedures (TTP) followed by an adversary based on MITRE ATT&CK.");
        print("[+] Author: lehag\n")

        ## Read the Tactics
        print("[+] TACTICS");
        with open("TTP/Tactics.json") as fd:
            tactics = json.load(fd);
            for i in tactics["Tactic"]:
                print("\t" + i["ID"] + " - " + i["Name"]);
        id = input("\t[>] Select the Tactic-ID you wish to test in your environment: ");

        ## Read the Techniques
        for i in tactics["Tactic"]:
            if i["ID"] == id:
                break;
        print("[+] TECHNIQUES");
        print("\t" + i["ID"] + " - " + i["Name"]);
        print("\tDescription: " + i["Description"] + "\n");
        with open(i["Path"]) as fd:
            tech = json.load(fd);
            for i in tech["Technique"]:
                print("\t" + i["ID"] + " - " + i["Name"]);
        id = input("\t[>] Select the Technique-ID you wish to test in your environment: ");

        ## Read the SubTechniques
        for i in tech["Technique"]:
            if i["ID"] == id:
                break;
        print("[+] SUBTECHNIQUES");
        print("\t" + i["ID"] + " - " + i["Name"]);
        print("\tDescription: " + i["Description"] + "\n");
        with open(i["Path"]) as fd:
            tech = json.load(fd);
            for i in tech["SubTechnique"]:
                print("\t" + i["ID"] + " - " + i["Name"]);
        id = input("\t[>] Select the SubTechnique-ID you wish to test in your environment: ");

        ## Read the Procedure
        for i in tech["SubTechnique"]:
            if i["ID"] == id:
                break;
        print("[+] PROCEDURES");
        print("\t" + i["ID"] + " - " + i["Name"]);
        print("\tDescription: " + i["Description"] + "\n");
        for j in i["Procedure"]:
            print("\t" + j["ID"] + " - " + j["Process"] + " " + j["Commandline"]);
        id = input("\t[>] Select the Procedure-ID you wish to test in your environment: ");
        
        ## Execute the Procedure
        for j in i["Procedure"]:
            if j["ID"] == id:
                break;
        print("[...] Executing the TTP.");
        process = j["Process"];
        commandline = j["Commandline"];
        args = process + " " + commandline; 
        result = subprocess.run(args);
