# -*- coding: utf-8 -*-
import os
import codecs
import sys
import re
import datetime
from lxml import etree

def getTextID(txt):
    txtgp = re.search("_LT\[xml.[^\.]*.([0-9]+)\]", txt)
    if txtgp is None:
        return ""
    return int(txtgp.group(1))

def getTextFromDict(dic, tID):
    if tID in dic:
        return dic[tID]
    else:
        return ""

targetName = "minimapinfo"
targetTXTName = targetName
localeName = ""
outputName = "Mabi_Minimapinfo"

dataDBText = {}
dataDB = {}

hasTXT = False
hasXML = False
fileList = os.listdir("./data/")
for fileN in fileList:
    if hasXML and hasTXT:
        break
    txtNameMatch = re.match(targetTXTName+".([a-zA-Z]*).txt", fileN)
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
    print("Missing "+targetTXTName+" TXT file.")
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
parser = etree.XMLParser(recover=True)
tree = etree.parse("./data/" + infilename, parser)
root = tree.getroot()
for elelist in list(root):
    if elelist.tag == "SearchExceptRegionList":
        continue
    for ele in elelist:
        ID = int(ele.attrib["RegionID"])

        if "MapName" in ele.attrib:
            NameID = getTextID(ele.attrib["MapName"])
            Name = getTextFromDict(dataDBText, NameID)

            LocalName = ""
            if "MapLocalName" in ele.attrib:
                LocalNameID = getTextID(ele.attrib["MapLocalName"])
                LocalName = getTextFromDict(dataDBText, LocalNameID)

            finalName = "No." + str(ID)
            if LocalName != "":
                finalName = LocalName
            elif Name != "":
                finalName = Name
        elif "FieldID" in ele.attrib:
            finalName = getTextFromDict(dataDB, int(ele.attrib["FieldID"]))+"_No."+str(ID)

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