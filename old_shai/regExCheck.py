import re

def termCheck(patterns,line):
    newDict = {}
    for pattern in patterns:
        for score in patterns[pattern]:
            regex = patterns[pattern][score]
            emails = re.findall(f"\s{regex}",line)
    newDict.update({pattern:{len(emails)*score:emails}}  )  

    return newDict 


# abc = ' guasassru@google.ie, careerguru99@hotmail.com, guru99@google.uk, '
# patterns = [{'emailsFound': {100: '[\\w\\.-]+@[\\w\\.-]+'}},{'urlsFound': {50: '(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))'}}]
# print(termCheck(patterns,abc))
