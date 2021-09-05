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
        self.TacticID = "";
        self.TechniqueID = "";
        self.SubTechniqueID = "";
        self.ProcedureID = "";

    def startAPT(self):
        """
            This is the main method of the A.P.T framework, it starts the remaining methods. 
        """
        self.displayDescription();
        self.loadTTP();
        
        while(True):
            apt.displayTactics();
            if(self.TacticID in self.TTPData):
                self.displayTechniques();
                if(self.TechniqueID in self.TTPData[self.TacticID]["Technique"]):
                    if("SubTechnique" in self.TTPData[self.TacticID]["Technique"][self.TechniqueID]):
                        self.displaySubTechniques();
                        if(self.SubTechniqueID in self.TTPData[self.TacticID]["Technique"][self.TechniqueID]["SubTechnique"]):
                            self.displayProcedures();
                        elif(self.SubTechniqueID == "E"):
                            print("Bye!");
                            exit(0);
                        else:
                            print("\t[-] SubTechnique ID not found");
                            continue;
                    else:
                        self.displayProcedures();
                elif(self.TechniqueID == "E"):
                    print("Bye!");
                    exit(0);
                else:
                    print("\t[-] Technique ID not found");
                    continue;
            elif(self.TacticID == "E"):
                print("Bye!");
                exit(0);
            else:
                print("\t[-] Tactic ID not found");
                continue;

    def displayDescription(self):
        """
            This method displays the description of the A.P.T framework.
        """
        print("""
            ╔═╗┌┬┐┬  ┬┌─┐┌┐┌┌─┐┌─┐┌┬┐  ╔═╗┌─┐┬─┐┌─┐┬┌─┐┌┬┐┌─┐┌┐┌┌─┐┌─┐  ╔╦╗┌─┐┌─┐┌┬┐┬┌┐┌┌─┐
            ╠═╣ ││└┐┌┘├─┤││││  ├┤  ││  ╠═╝├┤ ├┬┘└─┐│└─┐ │ ├┤ ││││  ├┤    ║ ├┤ └─┐ │ │││││ ┬
            ╩ ╩─┴┘ └┘ ┴ ┴┘└┘└─┘└─┘─┴┘  ╩  └─┘┴└─└─┘┴└─┘ ┴ └─┘┘└┘└─┘└─┘   ╩ └─┘└─┘ ┴ ┴┘└┘└─┘
        """);
        print("[+] Description: This project (WIP) aims to be a framework composed of modules that allow blue teams to test their threat detection capabilities in their environments by emulating the Tactics, Techniques and Procedures (TTP) followed by an adversary based on MITRE ATT&CK.");
        print("[+] Author: @lehag07\n");

    def loadTTP(self):
        """
            This method loads the Tactics, Techniques and Procedures stored in the file "TTP.json". 
        """
        try:
            with open(self.TTP) as fd:
                self.TTPData = json.load(fd);
        except Exception as e:
            print("\tError loading file 'TTP.json': " + str(e));
            exit(0);

    def displayTactics(self):
        """
            This method displays the Tactics available in the A.P.T framework.
        """
        print("[+] TACTICS");
        for id in self.TTPData:
            print("\t" + id + " : " + self.TTPData[id]["Name"]);
        print("\tE - Exit");
        self.TacticID = input("\n\tTTP> ");

    def displayTechniques(self):
        """
            This method displays the Techniques available in the A.P.T framework.
        """
        print("[+] TECHNIQUES");
        for id in self.TTPData[self.TacticID]["Technique"]:
            print("\t" + id + " : " + self.TTPData[self.TacticID]["Technique"][id]["Name"]);
        print("\tE - Exit");
        self.TechniqueID = input("\n\tTTP>" + self.TacticID + ">");

    def displaySubTechniques(self):
        """
            This method displays the SubTechniques available in the A.P.T framework.
        """
        print("[+] SUBTECHNIQUES");
        for id in self.TTPData[self.TacticID]["Technique"][self.TechniqueID]["SubTechnique"]:
            print("\t" + id + " : " + self.TTPData[self.TacticID]["Technique"][self.TechniqueID]["SubTechnique"][id]["Name"]);
        print("\tE - Exit");
        self.SubTechniqueID = input("\n\tTTP>" + self.TacticID + ">" + self.TechniqueID + ">");

    def displayProcedures(self):
        """
            This method displays the Procedures available in the A.P.T framework.
        """
        print("[+] PROCEDURES");
        for id in self.TTPData[self.TacticID]["Technique"][self.TechniqueID]["SubTechnique"][self.SubTechniqueID]["Procedure"]:
            print("\t" + id + " : " + self.TTPData[self.TacticID]["Technique"][self.TechniqueID]["SubTechnique"][self.SubTechniqueID]["Procedure"][id]);
        print("\tE - Exit");
        self.ProcedureID = input("\n\tTTP>" + self.TacticID + ">" + self.TechniqueID + ">" + self.SubTechniqueID + ">");

if __name__ == "__main__":
    apt = APT();
    apt.startAPT();
