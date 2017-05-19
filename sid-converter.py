#!/usr/bin/python

import fileinput
import re
	
f1 = raw_input("Enter the name of the rules file: ") 
fe_sid = raw_input("Enter last SID used in your policy: ")
f2 = open('fe_rules.txt', 'w+')

for line in fileinput.input(f1):

  if len(line.strip()) != 0:

    fe_sid = int(fe_sid)
    fe_sid = str(fe_sid + 1) 

# Need to add logic to detect number of digits in input sids

    line = re.sub('[0-9][0-9][0-9][0-9][0-9]', fe_sid, line.strip())

  f2.write(line)
f2.close()

print ('\nProcessing............................................')
print ('\nSID conversion for ' + f1 + ' completed succesfully \n')
print ('The new rules file is named fe_rules.txt \n')
