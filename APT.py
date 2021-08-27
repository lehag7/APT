#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    def __init__(self):
        self.TacticsPath = "TTP/Tactics.json";
        self.TacticsData = "";
        self.TacticID = "";
        self.TechniquesData = "";
        self.TechniqueID = "";
        self.SubTechniqueID = "";
        self.SubTechniquesData = "";
        self.ProcedureID = "";

    def displayDescription(self):
        print("""
            ╔═╗┌┬┐┬  ┬┌─┐┌┐┌┌─┐┌─┐┌┬┐  ╔═╗┌─┐┬─┐┌─┐┬┌─┐┌┬┐┌─┐┌┐┌┌─┐┌─┐  ╔╦╗┌─┐┌─┐┌┬┐┬┌┐┌┌─┐
            ╠═╣ ││└┐┌┘├─┤││││  ├┤  ││  ╠═╝├┤ ├┬┘└─┐│└─┐ │ ├┤ ││││  ├┤    ║ ├┤ └─┐ │ │││││ ┬
            ╩ ╩─┴┘ └┘ ┴ ┴┘└┘└─┘└─┘─┴┘  ╩  └─┘┴└─└─┘┴└─┘ ┴ └─┘┘└┘└─┘└─┘   ╩ └─┘└─┘ ┴ ┴┘└┘└─┘
        """);
        print("[+] Description: This project (WIP) aims to be a framework composed of modules that allow blue teams to test their threat detection capabilities in their environments by emulating the Tactics, Techniques and Procedures (TTP) followed by an adversary based on MITRE ATT&CK.");
        print("[+] Author: lehag\n");
    
    def loadTactics(self):
        print("[+] TACTICS");
        with open(self.TacticsPath) as fd:
            self.TacticsData = json.load(fd);
            for i in self.TacticsData["Tactic"]:
                print("\t" + i["ID"] + " - " + i["Name"]);
        print("\tE - Exit");
        self.TacticID = input("\n\tTTP> ");

    def loadTechniques(self):
        for i in self.TacticsData["Tactic"]:
            if i["ID"] == self.TacticID:
                break;
        print("[+] TECHNIQUES");
        with open(i["Path"]) as fd:
            self.TechniquesData = json.load(fd);
            for i in self.TechniquesData["Technique"]:
                print("\t" + i["ID"] + " - " + i["Name"]);
        self.TechniqueID = input("\n\tTTP>" + self.TacticID + "> Select the Technique-ID: ");

    def loadSubTechniques(self):
        for i in self.TechniquesData["Technique"]:
            if i["ID"] == self.TechniqueID:
                break;
        print("[+] SUBTECHNIQUES");
        with open(i["Path"]) as fd:
            self.SubTechniquesData = json.load(fd);
            for i in self.SubTechniquesData["SubTechnique"]:
                print("\t" + i["ID"] + " - " + i["Name"]);
        self.SubTechniqueID = input("\n\tTTP>" + self.TacticID + ">" + self.TechniqueID + "> Select the SubTechnique-ID: ");

    def loadProcedures(self):
        for i in self.SubTechniquesData["SubTechnique"]:
            if i["ID"] == id:
                break;
        print("[+] PROCEDURES");
        for j in i["Procedure"]:
            print("\t" + j["ID"] + " - " + j["Process"] + " " + j["Commandline"]);
        self.ProcedureID = input("\n\tTTP>" + self.TacticID + ">" + self.TechniqueID + ">" + self.SubTechniqueID + "> Select the Procedure-ID: ");

        for j in i["Procedure"]:
            if j["ID"] == self.ProcedureID:
                break;
        print("[...] Executing the TTP.");
        process = j["Process"];
        commandline = j["Commandline"];
        args = process + " " + commandline; 
        result = subprocess.run(args);

if __name__ == "__main__":
    apt = APT();
    apt.displayDescription();
    while(True):
        apt.loadTactics();
        apt.loadTechniques();
        apt.loadSubTechniques();
        apt.loadProcedures();
