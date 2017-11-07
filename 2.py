import os

a = '/home/lucy/Documents/code/python/exercise' 
os.chdir(a)
os.mknod("dummy.txt") #creating files
os.system("touch dummy2.txt") #creating files
print os.listdir(os.getcwd())

for f in os.listdir(a):
    f_name, f_ext = os.path.splitext(f) 
    print f_name

