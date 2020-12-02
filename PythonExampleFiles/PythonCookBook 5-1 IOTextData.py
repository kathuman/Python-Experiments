# Read the entire file as a single string
import os
import os.path
import glob

def main():
    with open("data.txt", 'rt') as f:
        data = f.read()
        print(data)

def main2(): 
    #This first instructiin is to list all the contents of a specific directory   
    names = os.listdir("c:\Python34")
    print(names)
    
    # In this case we only look for the directory components that end with .py
    pyfiles = [name for name in os.listdir("c:\Python34") if name.endswith(".py")]
    print(pyfiles)
    
    pyfiles = glob.glob("*.py")
    name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) for name in pyfiles]
    for name, size, mtime in name_sz_date:
        print(name, size, mtime)
    
    file_metadata = [(name, os.stat(name)) for name in pyfiles]
    for name, meta in file_metadata:
        print(name, meta.st_size, meta.st_mtime)

if __name__=="__main__":
#    main()
    main2()