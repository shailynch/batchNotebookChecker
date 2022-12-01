import re

def emailChecker(line):
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', line)
    emailsFound = len(emails)

    return emailsFound


# abc = 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
# print(emailChecker(abc))