from parse2 import read_csv
from put import dump
import ast
def main():
    input_file = 'file.csv'
    output_file = 'file.json'
    format = 'pretty'
    read_csv(input_file, output_file, format)
    with open(output_file) as f:
	flist=ast.literal_eval(f.read())
    dump(flist)

if __name__ == "__main__":
   main()
