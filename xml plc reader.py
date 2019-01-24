import xml.etree.ElementTree as ET
tree = ET.parse("input.L5X")

out1 = open("output.txt","w+")
out2 = open("output.csv","w+")

char_split = ["(",")",",",";","[","]","{","}"]

routines = []
tags = []

def getTagsList():
    # loops through every element and adds the element if its a tag
    tagsList = []
    for elem in tree.iter():
        if elem.tag == "Tag":
            tagsList.append(elem)
    return(tagsList)

def getRoutineList():
    # loops through every element and adds it if its a routine, in lists based on which routines it is in
    routinesList = []
    for elem in tree.iter():
        if elem.tag == "Routine":
            routinesList.append(elem)
    return(routinesList)

def getTagsInAllRoutines(routinesList, tags):
    tagsName = [tags[x].attrib["Name"] for x in range(len(tags))]
    blankList = [0 for _ in range(len(tags))]
    d = {}
    for i in range(len(routinesList)):
        d[routinesList[i].attrib["Name"]] = {}
        d[routinesList[i].attrib["Name"]] = dict(zip(tagsName, blankList))
        for child in routinesList[i]:
            for child in child:
                for child in child:
                    if child.tag == "Text":
                        text = multisplit(child.text.replace("\n",""), char_split, "\\")
                        text = [name for name in text if name.strip()]
                        for str in text:
                            if str in tagsName:
                                d[routinesList[i].attrib["Name"]][str] += 1
    return(d)
    


def multisplit(inp, split_list, dummy_char):
    for str in split_list:
        inp = inp.replace(str,dummy_char)
    return(inp.split(dummy_char))

tags = getTagsList()
tagsName = [tags[x].attrib["Name"] for x in range(len(tags))]
routines = getRoutineList()

dic = getTagsInAllRoutines(routines, tags)

out1.write(str(dic))
lin = "," + ",".join(tagsName) + "\n"
for i in range(len(dic)):
    lin += str(routines[i].attrib["Name"])
    for j in range(len(dic[routines[i].attrib["Name"]])):
        lin += "," + str(dic[routines[i].attrib["Name"]][tagsName[j]])
    lin += "\n"
out2.write(lin)
