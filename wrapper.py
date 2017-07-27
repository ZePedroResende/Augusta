from parse2 import read_csv
from put import dump
import ast
import glob, os

for file in glob.glob("./*.csv"):
    print(file)

def main():
    input_files = ['file1.csv','file2.csv']
    input_file = 'file.csv'
    output_file = 'file.json'
    format = 'pretty'
    with open(output_file, "r+") as f:
	    l = []
	    f.seek(0)
	    f.truncate()
            f.write(str(l))
    for j in input_files:
	    read_csv(j, output_file, format)
    with open(output_file) as f:
	flist=ast.literal_eval(f.read())
    dump(flist)

if __name__ == "__main__":
   main()
