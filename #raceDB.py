# -*- coding: utf-8 -*-
import os
import codecs
import sys
import re
import datetime
import xml.etree.ElementTree as ET

def getTextID(txt):
    txtgp = re.search("_LT\[xml.[a-zA-Z]*.([0-9]+)\]", txt)
    return int(txtgp.group(1))

def getTextFromDict(dic, tID):
    if tID in dic:
        return dic[tID]
    else:
        return ""

targetName = "race"
targetTXTName = ""
outputName = "Mabi_Race"

dataDBText = {}
dataDB = {}

hasTXT = False
hasXML = False
fileList = os.listdir(".")
for fileN in fileList:
    if hasXML and hasTXT:
        break
    txtNameMatch = re.match(targetName+".[a-zA-Z]*.txt", fileN)
    if txtNameMatch is not None:
        targetTXTName = fileN
        hasTXT = True
        continue
    xmlNameMatch = re.match(targetName+".xml", fileN)
    if xmlNameMatch is not None:
        hasXML = True
        continue

if hasTXT is False:
    print("Missing "+targetName+" TXT file.")
    sys.exit()
if hasXML is False:
    print("Missing "+targetName+" XML file.")
    sys.exit()

today = datetime.datetime.now().strftime("%Y%m%d")
outdir = os.getcwd()+"/patch-"+today+"/mod/"
print("Output: " + outdir)
try:
    os.makedirs(outdir)
except:
    pass

#targetName.XXXXX.txt
infilename = targetTXTName
fi = codecs.open(infilename,'r', encoding="utf-16")
for line in fi:
    oline = re.match(r"([0-9]{0,8})\t(([^\r])+)\r\n", line)
    if oline is not None:
        dataDBText[int(oline.group(1))] = oline.group(2)
fi.close()
print(infilename + " processed.")

#targetName.xml
infilename = targetName + ".xml"
tree = ET.parse(infilename)
root = tree.getroot()
for elelist in list(root):
    if elelist.tag == "RaceList":
        for ele in elelist:
            ID = int(ele.attrib["ID"])

            if ID in dataDB.keys():
                continue

            LocalNameID = getTextID(ele.attrib["LocalName"])

            Name = ele.attrib["EnglishName"]
            LocalName = getTextFromDict(dataDBText, LocalNameID)

            finalName = "No. " + str(ID)
            if LocalName != "":
                finalName = LocalName
            elif Name != "":
                finalName = Name

            dataDB[ID] = finalName

print(infilename + " processed.")

dataIDs = list(dataDB.keys())
dataIDs.sort()

fo = codecs.open(outdir+outputName+".ini", 'w', encoding="utf-16")
fo.write("["+outputName+"]\r\n")
for key in dataIDs:
    fo.write(str(key)+"="+dataDB[key]+"\r\n")
fo.close()

print(outputName + ".ini generated.")
