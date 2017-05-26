# -*- coding: utf-8 -*-
import os
import codecs
import sys
import re
import datetime
import xml.etree.ElementTree as ET

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

targetName = "skillinfo"
targetTXTName = targetName
localeName = ""
outputName = "Mabi_Skillicon"

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
tree = ET.parse("./data/" + infilename)
root = tree.getroot()
for elelist in list(root):
    for ele in elelist:
        ID = int(ele.attrib["SkillID"])

        finalName = "0,0,0"
        if "ImageFile" in ele.attrib:
            imgName = ele.attrib["ImageFile"].lower()
            imgG = re.search("data/gfx/image/gui_icon_skill_([^\.]*).dds", imgName)
            if imgG != None:
                imgNameIdx = int(imgG.group(1))
                if "PositionX" in ele.attrib and "PositionY" in ele.attrib:
                    posX = int(ele.attrib["PositionX"])
                    posY = int(ele.attrib["PositionY"])
                    finalName = str(imgNameIdx)+','+str(posX)+','+str(posY)

        if ID in dataDB.keys():
            if "Locale" in ele.attrib:
                if ele.attrib["Locale"] != localeName:
                    continue

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