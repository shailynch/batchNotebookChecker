#!/bin/sh
# run this to see how the program operates, the below command is the command that a terminal shelll would require
papermill notebookChecker.ipynb outputNotebookMultiLine.ipynb -p notebookList '''./sampleNotebooks/sample1.ipynb
./sampleNotebooks/sample2.ipynb
./sampleNotebooks/sample3.ipynb''' -p disallowedTermsList '''
0,security,100,security des
1,class,200,class des
2,people,300,people des
3,adhesion,400,adhesion des
''' -p disallowedRegexList '''
0,[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net),100,Email Address des
1,(?P<url>https?://[^\s]+),50,URL des
2,\d+,50,Hard-coded Number des
'''
