# Mabinogi INI Script / Mabinogi INI 生成脚本
## 简介
用来从Mabinogi的xml和txt文件提取信息并生成可供[Tin](http://oman.ga/Tin)使用的ini文件的Python脚本。
适用于以下文件：
- itemdb.xml & itemdb.*LOCALE_NAME*.txt (物品信息)
- manualform.xml & manualform.*LOCALE_NAME*.txt (图纸样本信息)
- minimapinfo.xml & minimapinfo.*LOCALE_NAME*.txt (区域信息)
- optionset.xml & optionset.*LOCALE_NAME*.txt (释放信息)
- race.xml & race.*LOCALE_NAME*.txt (种族信息)
- characterstyle.xml & characterstyle.*LOCALE_NAME*.txt (脸型发型头型信息)
- faceemotion2.xml & faceemotion2.*LOCALE_NAME*.txt (眼型口型信息)
- dungeondb2.xml & dungeondb.*LOCALE_NAME*.txt (佑拉地下城信息)
- dungeon_ruin.xml & dungeon_ruin.*LOCALE_NAME*.txt (伊利亚遗迹信息)
- skillinfo.xml & skillinfo.*LOCALE_NAME*.txt (技能信息)

## 使用方法
 1. Clone或者[打包下载](https://github.com/kaneorotar/Mabinogi_INI_Script/archive/master.zip)本repo后解压到任意目录
 2. 安装[Python](https://www.python.org/downloads/)(2.X或3.X皆可，也可从其他途径安装)
 3. 在cmd中通过pip安装lxml模块(指令：```pip install lxml```)
 4. 将xml和txt文件从pack中提取出来并放置在*data*文件夹中
 5. 双击执行```run_scripts.bat```
 6. 脚本执行完后，ini文件会出现在```./patch-LOCALE_NAME-YYYYMMDD/mod/```文件夹中

---

## Introduction
Python (2.X/3.X) scripts that process xml and txt files in Mabinogi to generate [Tin](http://oman.ga/Tin)-friendly ini files.
Work on the following data files:
 - itemdb.xml & itemdb.*LOCALE_NAME*.txt (Item Info)
 - manualform.xml & manualform.*LOCALE_NAME*.txt (Blacksmith Manual and Tailoring Pattern Info)
 - minimapinfo.xml & minimapinfo.*LOCALE_NAME*.txt (Region Info)
 - optionset.xml & optionset.*LOCALE_NAME*.txt (Enchant Info)
 - race.xml & race.*LOCALE_NAME*.txt (Race Info)
 - characterstyle.xml & characterstyle.*LOCALE_NAME*.txt (Face, HairStyle & Head Info)
 - faceemotion2.xml & faceemotion2.*LOCALE_NAME*.txt (Eye & Mouth Style Info)
 - dungeondb2.xml & dungeondb.*LOCALE_NAME*.txt (Uladh Dungeon Info)
 - dungeon_ruin.xml & dungeon_ruin.*LOCALE_NAME*.txt (Iria Ruin Info)
 - skillinfo.xml & skillinfo.*LOCALE_NAME*.txt (Skill Info)

## Usage
 1. Clone this repo or [download as ZIP](https://github.com/kaneorotar/Mabinogi_INI_Script/archive/master.zip), extract the content to location of your choice
 1. Install [Python](https://www.python.org/downloads/) (2.X or 3.X)
 2. Install lxml package (cmd: ```pip install lxml```)
 3. Place the xml and txt files in the *data* folder
 4. Run 'run_scripts.bat'
 5. The ini files should be in the folder ```./patch-LOCALE_NAME-YYYYMMDD/mod/```
