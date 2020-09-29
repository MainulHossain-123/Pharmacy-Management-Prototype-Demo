import unittest 
import project 
f=open("database_proj",'a+')

    
class TestProject(unittest.TestCase) :
    
    
   def test_additem(self):
    global var
    f4=open("database_proj",'r')
    x=f4.read().splitlines()
    last_line= x[-1]
    num_lines = 0
    with open("database_proj", 'r') as f8:
         for line in f8:
            num_lines += 1
    var=num_lines-1
    v = list(last_line.split(" "))
    print (str(v[0]))
    print (str(v[1]))
    print (str(v[2]))
    print (str(v[3]))
    print (str(v[4]))
    
    
    
   def test_firstitem(self):
    global var
    var=0
    f.seek(var)
    c=f.readline()
    v=list(c.split(" "))
    print ('check if first item is correct')
    print (str(v[0]))
    print (str(v[1]))
    print (str(v[2]))
    print (str(v[3]))
    print (str(v[4]))
        
   def test_nextitem(self):
    global var
    print('check for next items')
    var=1
    f.seek(var)
    c=f.readlines()
    xyz = c[var]
    v = list(xyz.split(" "))
    print (str(v[0]))
    print (str(v[1]))
    print (str(v[2]))
    print (str(v[3]))
    print (str(v[4]))
    
    var=2
    f.seek(var)
    c=f.readlines()
    xyz = c[var]
    v = list(xyz.split(" "))
    print (str(v[0]))
    print (str(v[1]))
    print (str(v[2]))
    print (str(v[3]))
    print (str(v[4]))
    
    
   def test_lastitem(self):
    global var
    f4=open("database_proj",'r')
    x=f4.read().splitlines()
    last_line= x[-1]
    num_lines = 0
    with open("database_proj", 'r') as f8:
         for line in f8:
            num_lines += 1
    var=num_lines-1
    v = list(last_line.split(" "))
    print (str(v[0]))
    print (str(v[1]))
    print (str(v[2]))
    print (str(v[3]))
    print (str(v[4]))
    
        
        
        


if __name__ == '__main__':
    unittest.main()         
        