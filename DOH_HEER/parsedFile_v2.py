import tempfile
import sys
import os
import csv, sqlite3
import re

def create_db(filename):
      #strip extension out of filename to be used
      #as table name
      tableName = os.path.splitext(filename)[0]
      tableName = tableName.replace('-','_')
      con = sqlite3.connect("HEER.db")
      cur = con.cursor()
      headerInfo = ''
      with open(filename, 'r') as f:
           headerInfo = f.readline().strip()
      if headerInfo:
           dbExe = "CREATE TABLE " + tableName + " (" + headerInfo + ");"
           cur.execute(dbExe)

           with open(filename, 'r') as f:
                reader = csv.reader(f)
                for field in reader:
                    headerInfo = re.sub(r'c[0-9]*', '?', headerInfo)
                    dbExe = "INSERT INTO " + tableName + " VALUES (" + headerInfo + ");"
                    cur.execute(dbExe, field)

      con.commit()
      con.close()

def modify_file(filename):

      #Create temporary file read/write
      t = tempfile.NamedTemporaryFile(mode="r+")

      #Open input file read-only
      i = open(filename, 'r')

      startPrint = False

      #Copy input file to temporary file, modifying as we go
      for line in i:
           if 'ACENAPHTHENE' in line:
                # Prepend generic header info in front of file
                tempString = ''
                for count in range(1, len(line.split(','))+1):
                    tempString = tempString + "c"+str(count)+","
                t.write(tempString[:-1]+"\n") #remove last not needed comma char
                startPrint = True
           if 'ZINC' in line:
                t.write(line)
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
            create_db(filename)
