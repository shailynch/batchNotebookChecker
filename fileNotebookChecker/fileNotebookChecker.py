#forbidden words function
def checkTerms(line, deniedTerms): 
    import re
    #denied terms = list of terms to be checked e.g ['this', 'style', 'layout']
    #line takes any line to be checked this format doesn't matter but prefers string
    terms_count = {term : 0 for term in deniedTerms}
    for term in deniedTerms:
                #loop through terms 
                if re.search(term,line, re.IGNORECASE):
                    #check term in line
                    terms_count[term] += 1
#                     print(terms_count) #to see this carried out line by line
    return terms_count

def displayResults(terms_count):
    import pandas as pd
    import matplotlib.pyplot as plt
    orderedResults = { term:score for term,score in sorted(terms_count.items(), key=lambda item:item[1])}
    df = pd.DataFrame.from_dict(orderedResults, orient='index', columns=[('Total Score')])

    f = plt.figure()
    f.set_figwidth(3)
    f.set_figheight(5)
    plt.bar(range(len(orderedResults)),list(orderedResults.values()),align='center',color=['r','g','b'])
    plt.xticks(range(len(orderedResults)),list(orderedResults.keys()))
    plt.xlabel('Notebook Names')
    plt.ylabel('Score')
    plt.show
    
    return df


def evaluateNotebook(directory,filename):
    import shutil
    import os 

    original = str(directory) +'/' + str(filename)
    target = str(directory) +'/evaluated' + str(filename)

    try:
      shutil.copyfile(original, target)
    except:
        print("something went wrong")
  
    # evaluation = "here we take the path only and evaluate the notebook"
    deniedTerms = ['security', 'war','asylum']
    terms_count = {term : 0 for term in deniedTerms}
    file = open(target, "r")
    for line in file:
        results = checkTerms(line,deniedTerms)
        for term in results:
            if results[term] >0:
                terms_count[term] += results[term]

    file.close()
    try:
            os.remove(str(target))
    except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))

    print(displayResults(terms_count))
    return terms_count


def evaluateNotebookWithList(directory, filename,deniedTerms):
    import shutil
    import os 

    original = str(directory) +'/' + str(filename)
    target = str(directory) +'/evaluated' + str(filename)

    try:
      shutil.copyfile(original, target)
    except:
        print("something went wrong")
  
    # evaluation = "here we take the path only and evaluate the notebook"
    terms_count = {term : 0 for term in deniedTerms}
    file = open(target, "r")
    for line in file:
        results = checkTerms(line,deniedTerms)
        for term in results:
            if results[term] >0:
                terms_count[term] += results[term]

    file.close()
    try:
            os.remove(str(target))
    except OSError as e:  ## if failed, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))

    print(displayResults(terms_count))
    return terms_count