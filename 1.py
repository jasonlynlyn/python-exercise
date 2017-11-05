#OS for files
import os
from datetime import datetime

print dir(os)#all attributes/methods in os
print os.getcwd()#current working directory

a='/home/lucy/Documents/code/python/exercise'
os.chdir(a)#change dir
#get home envar path
print os.environ.get('HOME')

#create a file in HOME
file_path = os.path.join(os.environ.get('HOME'), 'main.txt')
print file_path

b='/tmp/main.txt'
print os.path.basename(b)
print os.path.exists(b)
print os.path.isdir(b)
print os.path.isfile(b)
print os.path.splitext(b) #split file name and extension
print dir(os.path)


#create dir
os.mkdir('dummy')
os.makedirs('dummy1/dummy2')

# #delete dir
os.rmdir('dummy')
os.removedirs('dummy1/dummy2')

# #rename
os.rename('draft.py', 'rename.py')

# #read file
print os.stat('rename.py')

# #modification time
mod_time=os.stat('rename.py').st_mtime
print datetime.fromtimestamp(mod_time)

print os.getcwd()#show current dir
print os.listdir(a)#ls a dir

# #file searching
for dirpath, dirnames, filenames in os.walk(a):
    print ("Current path: ", dirpath) 
    print ("Directories: ", dirnames)
    print ("Files: ", filenames)
