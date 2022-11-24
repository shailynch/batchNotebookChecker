

#forbidden words function
def termCheck(deniedTerms, line): 
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
