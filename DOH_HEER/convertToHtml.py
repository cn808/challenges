import sys
import os
import subprocess
import re

if __name__ == "__main__":
	csvToTableExeLoc = 'C:\\Python27\\Scripts\\'
	inputOutputLoc = 'C:\\Users\\017974\\Downloads\\ParsedFullSurferCSV\\'
	for filename in os.listdir(sys.argv[1]):
			if filename.endswith(".csv"): 
				htmlName = re.sub(r'csv', 'html', filename)
				args = [csvToTableExeLoc + 'csvtotable', inputOutputLoc + filename, inputOutputLoc + htmlName]
				subprocess.call( args )
            
