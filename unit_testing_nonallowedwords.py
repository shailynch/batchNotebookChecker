# function to check non allowed words
def checkword(non_allowed_word,codeline):
    # breaking down the non allowed words list
    index_list = non_allowed_word[0::3]
    word_list = non_allowed_word[1::3]
    weight_list = non_allowed_word[2::3]
    
    # Output variables
    code_line_num = 0
    rule_type = "non_allowed_word"
    rule_num = 0
    output_list = []
    word_list_lower = []

    # converting words in lower case
    for word in word_list:
        word_list_lower.append(word.lower())
       # print(word_list_lower)

    # looping through every line from word list 
    for line in word_list_lower:
        # print(line)
        # geting code line number
        code_line_num = word_list_lower.index(line)

        # checking if our words exist in word list
        if line in word_list_lower:
            # print("exist")
            # calculating rule number and rule weight
            rule_num = word_list_lower.index(line)
            rule_weight = weight_list[rule_num]

            # Append to output list
            output_list.append(code_line_num)
            output_list.append(rule_type)
            output_list.append(rule_num)
            output_list.append(rule_weight)
        else:
            # print("not exist")
            pass

    # If no line matches a pattern/rule, the output list will be empty
    if not output_list:
        print("no word match")
        return(output_list)
    else:
        # Output list to be returned
        # print(output_list)
        return(output_list)

