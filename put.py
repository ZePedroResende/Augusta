#!/usr/bin/python
import json 
import ast
from pymongo import MongoClient

def main():
	input_file = 'file.json'
	with open(input_file) as f:
		flist=ast.literal_eval(f.read())
	dump(flist)

def classify(j):
	with open('config.json') as json_data:
		d = json.load(json_data)
	for key,value in j.items():	
		maximo = int (d[key]['maximo'])
		minimo = int (d[key]['minimo'])
		valor = int(value)	
		if (minimo > valor or valor > maximo):
			return False
	return True 

def dump(l):
	client = MongoClient()
	db = client['augusta']
	normal= db['normal']	
	teste = db['teste']	
	quarentena= db['quarentena']	
	for item in l :
		if classify(item):
			normal.insert_one(item)
		else:
			quarentena.insert_one(item)

if __name__ == "__main__":	
	main()
