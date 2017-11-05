#look for a specific directory, if exists, list all

import os

#go to the dir
a = '/home/lucy/Documents/codes/'
n=os.path.exists(a)

if n == True:
    print os.path.splitext(a) #see file type
else:
    print "No such directory"



