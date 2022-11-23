def emailChecker(line):
    import re
    emailRegex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    email = re.findall(emailRegex,line)
    if not email:
        email_found = False
    else:
        email_found = True
    return email_found
# example
# print ( emailChecker('shai.lynch.sl@gmail.com'))
