#!/usr/bin/python
import sys, getopt
import csv
import ast
import json

def main():
    input_file = 'file.csv'
    output_file = 'file.json'
    format = 'pretty'
    read_csv(input_file, output_file, format)

def read_csv(file, json_file, format):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        title = reader.fieldnames
        for row in reader:
            csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
        write_json(csv_rows, json_file, format)
def concatL(a, b):
	return [j for i in zip(a,b) for j in i]


def write_json(data, json_file,format):
    with open(json_file, "r+") as f:
	    flist = ast.literal_eval(f.read())
            data = rem(data)
	    #data  = concatL(data,flist)
	    data = data +flist
            j = json.dumps(data,sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False)
	    f.seek(0)
	    f.truncate()
            f.write(j)

def write_json1(data, json_file, format):
    with open(json_file, "w") as f:
        if format == "pretty":
            data = rem(data)
            j = json.dumps(data,sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False)
            f.write(j)
        else:
            f.write(json.dumps(data))

def rem(data):
    newList= []
    for d in data :
        for i in xrange(len(d)):
            if d.values()[i] == "":
                break
            else:
                if(i+1 == (len(d))):
                    newList.append(d) 
                else:
                    continue
    return newList
 #return [d for d in data if d.values()[0] != ""] 
    
def remove_invalid(json):
    for i in xrange(len(json)):
            print(json[0])
            if json[0] == "":
                json.pop(i)
                break
    return json

if __name__ == "__main__":
   main()
