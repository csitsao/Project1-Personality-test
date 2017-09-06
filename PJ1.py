def sortedPercentage(line):
    linelist = list(line) # turn a string into a list of characters
    extrointro = []
    senintu = []
    thinkfeel = []
    judgeprece = []

    for i in range(7):
        for j in range(10):
            if (i*10+j) % 7 == 0: # for E or I
                extrointro.append(linelist[i*10+j])
            elif (i*10+j) % 7 == 1 or (i*10+j) % 7 == 2: # for S or N
                senintu.append(linelist[i*10+j])
            elif (i*10+j) % 7 == 3 or (i*10+j) % 7 == 4: # for T or F
                thinkfeel.append(linelist[i*10+j])
            elif (i*10+j) % 7 == 5 or (i*10+j) % 7 == 6: # for J or P
                judgeprece.append(linelist[i*10+j])
    # print extrointro, senintu, thinkfeel, judgeprece

    ei = abPercentages(extrointro)
    sn = abPercentages(senintu)
    tf = abPercentages(thinkfeel)
    jp = abPercentages(judgeprece)
    percentage = [ei, sn, tf, jp]
    return percentage

def abPercentages(lists): # For b percentage
    import math
    bcounter = 0
    acounter = 0
    for x in lists:
        if x == "B" or x == "b":
            bcounter += 1
        elif x == "A" or x == "a":
            acounter += 1
    counter = acounter + bcounter # only actual answers count
    num = float(bcounter*100)/counter # if no float, it will just turn into integer with rounding down

    if num + 0.5 >= math.floor(num) + 1: # rounding numbers
        num = math.ceil(num) # rounding up
    else:
        num = math.floor(num) # rounding down
    return int(num)

def persona(percentage): # For printing the final personality string
    # print percentage
    persona = []
    persona.append(extroORintro(percentage[0]))
    persona.append(senORintu(percentage[1]))
    persona.append(thinkORfeel(percentage[2]))
    persona.append(judgeORprece(percentage[3]))s
    return ("").join(persona) # joining a list back to a string

# Functions for determining characters for personality
def extroORintro(ei):
    if ei > 50:
        return "I"
    elif ei == 50:
        return "X"
    else:
        return "E"
def senORintu(sn):
    if sn > 50:
        return "N"
    elif sn == 50:
        return "X"
    else:
        return "S"
def thinkORfeel(tf):
    if tf > 50:
        return "F"
    elif tf == 50:
        return "X"
    else:
        return "T"
def judgeORprece(jp):
    if jp > 50:
        return "P"
    elif jp == 50:
        return "X"
    else:
        return "J"


# Check results at https://courses.cs.washington.edu/courses/cse142/17su/diff.html.
#-------------------------------------------------------------------------------

print """
This program processes a file of answers to the Keirsey Temperament Sorter.
It converts the various A and B answers for each person into a sequence of
B-percentages and then into a four-letter personality type.

Please enter the name of your file that you would like to process:
"""

filename = raw_input("> ") # collecting input file name and open
inputfile = open(filename, "r")

print """
Please enter the name of your output file:
"""
output = raw_input("> ") # collecting output file name and open
outputfile = open(output, "w")

for line in inputfile: # formatting output file
    if len(line) < 70:
        outputfile.write(line.rstrip('\r\n')) # .rstrip() removes characters from the end (right side)
        outputfile.write(": ")
    else:
        percentage = sortedPercentage(line)
        outputfile.write(str(percentage)) # to write a list in file (turn list into string)
        outputfile.write(" = ")
        outputfile.write(persona(percentage))
        outputfile.write("\n")

inputfile.close()
outputfile.close()
