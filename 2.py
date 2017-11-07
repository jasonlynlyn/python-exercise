import os

a = '/home/lucy/Documents/code/python/exercise' 
os.chdir(a)
print os.listdir(os.getcwd())

for f in os.listdir(a):
    f_name, f_ext = os.path.splitext(f) 
    print f_name

