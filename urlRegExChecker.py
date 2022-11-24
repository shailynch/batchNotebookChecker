
#url emails - extra functionality online datasets and csv checks
def urlChecker(line):
    import re
    urlRegex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(urlRegex,line) 
    url_found = True
    if not url:
        url_found = False
    
    return url_found
# example
# print(urlChecker('https://www.asda.ie'))

