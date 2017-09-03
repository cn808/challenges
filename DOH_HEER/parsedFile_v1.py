fout = open('parsedFile.csv', 'w')
f = open('TableA-1.csv', 'r')
startPrint = False

for line in f:
    if 'CHEMICAL PARAMETER' in line or 'CONTAMINANT' in line:
        startPrint = True
    if 'Notes' in line:
        startPrint = False
    if startPrint and line.strip():
        fout.write(line)

f.close()
fout.close()
