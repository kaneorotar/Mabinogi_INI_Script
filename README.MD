# Mabinogi INI Script

Python (2.X/3.X) scripts that process xml and txt files in Mabinogi to generate [Tin](http://www.yydzh.com/read.php?tid=1928854)-friendly ini files. 
Work on the following data files:
 - itemdb.xml & itemdb.*LOCALE_NAME*.txt (Item Info)
 - manualform.xml & manualform.*LOCALE_NAME*.txt (Blacksmith Manual and Tailoring Pattern Info)
 - minimapinfo.xml & minimapinfo.*LOCALE_NAME*.txt (Region Info)
 - optionset.xml & optionset.*LOCALE_NAME*.txt (Enchant Info)
 - race.xml & race.*LOCALE_NAME*.txt (Race Info)
 - characterstyle.xml & characterstyle.*LOCALE_NAME*.txt (Face, HairStyle & Head Info)
 - faceemotion2.xml & faceemotion2.*LOCALE_NAME*.txt (Eye & Mouth Style Info)

### Usage

 1. Install Python (2.X or 3.X)
 2. Place the xml and txt files in the *data* folder
 3. Run 'run_scripts.bat'
 4. The ini files should be in the folder './patch-LOCALE_NAME-YYYYMMDD/mod/'