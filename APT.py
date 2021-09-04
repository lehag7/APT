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
        self.TTP = "TTP.json";
        self.TTPData = "";
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
        with open(self.TTP) as fd:
            self.TTPData = json.load(fd);
        
        for id in self.TTPData:
            print("\t" + id + " : " + self.TTPData[id]["Name"]);
        print("\tE - Exit");
        self.TacticID = input("\n\tTTP> ");
        return self.TacticID;

    def loadTechniques(self, TacticID):
        print("[+] TECHNIQUES");

        for id in self.TTPData[self.TacticID]["Technique"]:
            print("\t" + id + " : " + self.TTPData[self.TacticID]["Technique"][id]["Name"]);
        print("\tE - Exit");
        self.TechniqueID = input("\n\tTTP>" + self.TacticID + ">");
        return self.TechniqueID;

    def loadSubTechniques(self, TechniqueID):
        for i in self.TechniquesData["Technique"]:
            if i["ID"] == self.TechniqueID:
                break;
        print("[+] SUBTECHNIQUES");
        for i in self.TacticsData["Tactic"]:
            if(i["ID"] == TacticID):
                for j in i["Technique"]:
                    if(j["ID"] == TechniqueID):
                        for k in j["Subtechnique"]:
                            print("\t" + j["ID"] + " - " + j["Name"]);


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
        TacticID = apt.loadTactics();
        if(TacticID != "E"):
            TechniqueID = apt.loadTechniques(TacticID);
            exit(0);
            if(TechniqueID != "E"):
                SubTechniqueID = 3;
                if(SubTechniqueID == None):
                    apt.loadSubTechniques();
                    apt.loadProcedures();
            else:
                exit(0);
        else:
            exit(0);
