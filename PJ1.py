print """
This program processes a file of answers to the Keirsey Temperament Sorter.
It converts the various A and B answers for each person into a sequence of
B-percentages and then into a four-letter personality type.

Please enter the name of your file that you would like to process:
"""

filename = raw_input("> ")
inputfile = open(filename, "r")

# inputfile.readlines() # This turn all the lines into a list

names = []
results = []

for line in inputfile:
    if len(line) < 70:
        names.append(line)









inputfile.close()
