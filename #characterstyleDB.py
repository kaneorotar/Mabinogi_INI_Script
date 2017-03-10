# -*- coding: utf-8 -*-
import os
import codecs
import sys
import re
import datetime
import xml.etree.ElementTree as ET

def getTextID(txt):
    txtgp = re.search("_LT\[xml.[a-zA-Z0-9]*.([0-9]+)\]", txt)
    return int(txtgp.group(1))

def getTextFromDict(dic, tID):
    if tID in dic:
        return dic[tID]
    else:
        return ""

targetName = "characterstyle"
targetTXTName = ""
localeName = ""
outputName = "Mabi_Characterstyle"

dataDBText = {}
dataDB = {}

hasTXT = False
hasXML = False
fileList = os.listdir("./data/")
for fileN in fileList:
    if hasXML and hasTXT:
        break
    txtNameMatch = re.match(targetName+".([a-zA-Z]*).txt", fileN)
    if txtNameMatch is not None:
        targetTXTName = fileN
        localeName = txtNameMatch.group(1)
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
outdir = os.getcwd()+"/patch-"+localeName+"-"+today+"/mod/"
print("Output: " + outdir)
try:
    os.makedirs(outdir)
except:
    pass

#targetName.XXXXX.txt
infilename = targetTXTName
fi = codecs.open("./data/" + infilename,'r', encoding="utf-16")
for line in fi:
    oline = re.match(r"([0-9]{0,8})\t(([^\r])+)\r\n", line)
    if oline is not None:
        dataDBText[int(oline.group(1))] = oline.group(2)
fi.close()
print(infilename + " processed.")

#targetName.xml
infilename = targetName + ".xml"
tree = ET.parse("./data/" + infilename)
root = tree.getroot()
for elelist in list(root):
    tempDB = {}
    for ele in elelist:

        if "ID" not in ele.attrib:
            continue

        ID = int(ele.attrib["ID"])

        if ID in tempDB.keys():
            continue

        NameID = getTextID(ele.attrib["Name"])

        Name = getTextFromDict(dataDBText, NameID)

        finalName = "No."+ str(ID)
        if Name != "":
            finalName = Name

        tempDB[ID] = finalName
    dataDB[elelist.tag] = tempDB

print(infilename + " processed.")

dataIDs = list(dataDB.keys())
dataIDs.sort()


for key in dataIDs:
    tempIDs = list(dataDB[key].keys())
    if len(tempIDs) == 0:
        continue
    tempIDs.sort()
    fo = codecs.open(outdir+"Mabi_"+key+".ini", 'w', encoding="utf-16")
    fo.write("["+key+"]\r\n")
    for subkey in tempIDs:
        fo.write(str(subkey)+"="+dataDB[key][subkey]+"\r\n")
    fo.close()
    print("Mabi_"+ key + ".ini generated.")