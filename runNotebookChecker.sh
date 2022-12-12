#!/bin/sh
papermill notebookChecker.ipynb output.ipynb -p notebookList '''./sampleNotebooks/sample1.ipynb
./sampleNotebooks/sample2.ipynb
./sampleNotebooks/sample3.ipynb''' -p disallowedTermsList '''
0,security,100,security des
1,class,200,class des
2,people,300,people des
3,adhesion,400,adhesion des
'''

