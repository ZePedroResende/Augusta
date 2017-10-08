#!/usr/bin/python
import sys, getopt
import csv
import ast
import json
import __builtin__
from extraString import ExtraString
__builtin__.dict = ExtraString

class Parse:
    def __init__(self):
        self.data = []

    def read_csv(self, file):
        csv_rows = []
        with open(file) as csvfile:
            reader = csv.DictReader(csvfile)
            title = reader.fieldnames
            for row in reader:
                csv_rows.extend([{title[i]:row[title[i]] for i in range(len(title))}])
            self.write_json(csv_rows)

    def write_json(self, data):
        self.rem()
        self.data =  self.data + (data)
        j = json.dumps( self.data,sort_keys=False, indent=4, separators=(',', ': '),encoding="utf-8",ensure_ascii=False)
        self.data = j

    def rem(self):
        data = self.data
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

    def testDump(self):
        data = ast.literal_eval(self.data)
        normal = open("normal.log","w")
        quarentena= open("quarentena.log","w")
        try:
            for item in data:
                if item.classify():
                    json.dump(item,normal)
                    normal.write("\n")
                else:
                    json.dump(item,quarentena)
                    quarentena.write("\n")
        finally:
            normal.close()
            quarentena.close()
'''
tem de ser feito com um botao
    def dump(self):
        client = MongoClient()
        db = client['augusta']
        normal= db['normal']
        teste = db['teste']
        quarentena= db['quarentena']
        normal = open("normal.log")
        quarentena= open("quarentena.log")
        for item in self.data :
            item.__class___ = extraString
            if item.classify():
                with open("log","a") as f:
                    json.dump(item,f)
                    f.write("\n")
                    f.close()
                normal.insert_one(item)
            else:
                quarentena.insert_one(item)
'''
def main():
    print("ola")
    p = Parse()
    p.read_csv("../etc/file1.csv")
    p.testDump()
