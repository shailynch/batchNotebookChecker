import re

# Check inpout lines against input patterns/rules
def checkRegex(patternList, line):
    outputList = {pattern : 0 for pattern in patternList}
    # Return if the line matches the current pattern
    for pattern in patternList:
        searchResults = re.findall(pattern, line)
        #print(searchResults)
        if len(searchResults) > 0:
            outputList[pattern] = len(searchResults)
            #print(outputList)
    return outputList