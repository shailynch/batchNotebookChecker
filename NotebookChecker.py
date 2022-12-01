import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import re
import os
import json
import codecs

from os import path

from RegEx_Checker_UT import check_lines_for_patterns
from unit_testing_nonallowedwords import checkword

#parameters for deny list and url 
denyListURL = "denylist.csv"
patternListURL = "regexPatterns.csv"
notebookListURL ="notebooklist.csv"

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

#notebook checker function 
def notebookChecker(denyListURL, patternListURL, notebookListURL):
    denyTerms = pd.read_csv(path.join(d, denyListURL))
    sortedList = pd.DataFrame(denyTerms, columns=['index','word','weight'])
    denylistTerms = sortedList.values.tolist()
    disallowedList = [item for sublist in denylistTerms for item in sublist]

    patternList = pd.read_csv(path.join(d, patternListURL))
    sortedPatternList = pd.DataFrame(patternList, columns=['index','pattern','weight'])
    patternlistTerms = sortedPatternList.values.tolist()
    regExPatternList = [item for sublist in patternlistTerms for item in sublist]
    

    checkedNotebooks = {}
    
    notebookList = pd.read_csv(path.join(d, notebookListURL))
    uncheckedNotebooks = np.array(notebookList)
    # print (f"\n Here we open and read the notebooks due to be open {uncheckedNotebooks} \n")
    

    #loop through files from list
    for uncheckedNotebook in uncheckedNotebooks:
        notebook = {}
        # here we check line by line the the terms found which are added to a list 
        try:
            file = codecs.open(str(f"{path.join(d, uncheckedNotebook[0])}"), "r")
            source = file.read()
            y = json.loads(source)
            currentNotebook = []
            for x in y['cells']:
                for x2 in x['source']:
                    currentNotebook.append(x2)
        except:
            print("Can't read file")

        try:
            wordCheckerOutput = checkword(disallowedList, currentNotebook)
            if (wordCheckerOutput != None):
                # print("Word checker OUTPUT: ", wordCheckerOutput)
                pass
            else:
                print("Word check output is empty")
        except:
            print("Word checker went wrong")
        
        try:
            regExOutput = check_lines_for_patterns(regExPatternList, currentNotebook)
            if (regExOutput != None):
                # print("RegEx Checker OUTPUT: ", regExOutput)
                pass
            else:
                print("RegEx check output is empty")
        except:
            print("RegEx checker went wrong")

        notebook.update({"disallowed words": wordCheckerOutput})
        notebook.update({"regex patterns": regExOutput})
        checkedNotebooks.update({str(uncheckedNotebook): notebook})

    return checkedNotebooks 
        

notebookResults = notebookChecker(denyListURL, patternListURL, notebookListURL)
print(notebookResults)