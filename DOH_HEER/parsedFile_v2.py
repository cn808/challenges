import tempfile
import sys
import os

def modify_file(filename):

      #Create temporary file read/write
      t = tempfile.NamedTemporaryFile(mode="r+")

      #Open input file read-only
      i = open(filename, 'r')

      startPrint = False

      #Copy input file to temporary file, modifying as we go
      for line in i:
           if 'CHEMICAL PARAMETER' in line or 'CONTAMINANT' in line:
                startPrint = True
           if 'Notes' in line:
                startPrint = False
           if startPrint and line.strip():
                t.write(line)

      i.close() #Close input file

      t.seek(0) #Rewind temporary file to beginning

      o = open(filename, "w")  #Reopen input file writable

      #Overwriting original file with temporary file contents          
      for line in t:
           o.write(line)  

      t.close() #Close temporary file, will cause it to be deleted

if __name__ == "__main__":
    for filename in os.listdir(sys.argv[1]):
        if filename.endswith(".csv"): 
            modify_file(filename)