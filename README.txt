Use:

run xml plc reader.exe with input.L5X in the same folder and get output.txt in the format of a python dictionary and output.csv
if you want to use said dictionary in something include this code

import ast
inp = open("output.txt", "r")
d = ast.literal_eval(inp)

Original (vague) specifications:

Attached file is XML format
Create a Tag list
XML structure Tags\Tag Name=”tag name”, where heading <Tags> exists in a couple of different sections.
Create a routine list
XML structure Routines\Routine Name=”routine name”, where heading <Routines> exists in a couple of different sections.
For each Tag in tag list, count the number of times it is found in each routine
Routines\Routine\RLLContent\Rung, where heading <Routines> exists in a couple of different sections.
Save as a excel worksheet with tag names down the side and routines along the top and the count of tag names in the cells.
 