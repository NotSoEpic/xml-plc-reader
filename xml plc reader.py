import xml.etree.ElementTree as ET
tree = ET.parse("input.L5X")

out = open("output.txt","w+")

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
    listIndex = -1
    for elem in tree.iter():
        if elem.tag == "Routines":
            listIndex += 1
            routinesList.append(["dummy"])
            for child in elem:
                routinesList[listIndex].append(child)
            del routinesList[listIndex][0]
    return(routinesList)

def getTagsInAllRoutines(routinesList, tags):
    tagsName = [tags[x].attrib["Name"] for x in range(len(tags))]
    blankList = [0 for _ in range(len(tags))]
    d = {}
    for i in range(len(routinesList)):
        d[i] = {}
        d[i] = dict(zip(tagsName, blankList))
        for j in range(len(routinesList[i])):
            for child in routinesList[i][j]:
                for child in child:
                    for child in child:
                        if child.tag == "Text":
                            text = multisplit(child.text.replace("\n",""), char_split, "\\")
                            text = [name for name in text if name.strip()]
                            for str in text:
                                if str in tagsName:
                                    d[i][str] += 1
    return(d)
    


def multisplit(inp, split_list, dummy_char):
    for str in split_list:
        inp = inp.replace(str,dummy_char)
    return(inp.split(dummy_char))

tags = getTagsList()
routines = getRoutineList()

out.write(str(getTagsInAllRoutines(routines, tags)))
