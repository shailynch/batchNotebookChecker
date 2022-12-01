import re

# Check inpout lines against input patterns/rules
def check_lines_for_patterns(regex_pattern_list, code_lines):
    # Pattern list example: (1,RegEx,Weight, 2,RegEx2,Weight2)
    # Split pattern_list into separate lists
    # Starting at index 0 get every third item (0-3-6)
    index_list = regex_pattern_list[0::3]
    regex_list = regex_pattern_list[1::3]
    weight_list = regex_pattern_list[2::3]

    # Output variables
    code_line_num = 0
    rule_type = "RegEx"
    rule_num = 0
    output_list = []

    # Loop for every (code) line in our file
    for line in code_lines:
        # Keep track of line number
        code_line_num = code_lines.index(line)
        # print("code line num = ",code_line_num)

        # Loop for every RegEx pattern we are looking for
        for pattern in regex_list:
            # Keep track of rule number
            rule_num = regex_list.index(pattern)
            # print("rule num = ",rule_num)

            # Return if the line matches the current pattern
            if(re.findall(pattern, line)):
                # print("Code line matches a rule")
                # Uses the index of the rule number to find the corresponding rule weight
                rule_weight = weight_list[rule_num]
                # Append to output list
                output_list.append(code_line_num)
                output_list.append(rule_type)
                output_list.append(rule_num)
                output_list.append(rule_weight)
            else:
                # print("Code line does not match any rule")
                pass
    
    # If no line matches a pattern/rule, the output list will be empty
    if not output_list:
        print("No lines matched any rules!")
    else:
        # Output list to be returned
        return(output_list)
