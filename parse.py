import csv
import json

csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

next(csvfile,None)
fieldnames = ("Estacao","Parametro","Unidade","NValores","Data Inicio","Data Final")

reader = csv.DictReader(csvfile,fieldnames)

fieldnames = reader.fieldnames
for row in reader:
    print(row)
    print('\n')
    json.dump(row, jsonfile)
    jsonfile.write('\n')
