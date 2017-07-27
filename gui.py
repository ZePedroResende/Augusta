#!/usr/bin/python

from Tkinter import *
from pymongo import MongoClient
import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from wrapper import main

root = Tk()
root.title("Augusta")
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
	with open('log', "r+") as l:
		for line in l: 
		    lb.insert(END, line)
		l.seek(0)
		l.truncate()
		l.close()

def startW():
  threading.Timer(10.0, startW).start()
  main()

def Button1():
	startW()
#	client = MongoClient()
#	db = client['augusta']
#	normal= db['normal']	
#	for doc in normal.find():
	    # do things

def Button2():
	print "hello"
	#listbox.insert(END, "Stop")

def Button3():
	text_contents = text.get()
	listbox.insert(END, text_contents)
	text.delete(0,END)

button1 = Button(root, text="Start", command = Button1)
button2 = Button(root, text="Stop", command = Button2)
#button3 = Button(root, text="button3", command = Button3)

text = Entry(root)
scrollbar = Scrollbar(root, orient="vertical")
lb = Listbox(root, width=50, height=20, yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)

scrollbar.pack(side="right", fill="y")
lb.pack(side="left",fill="both", expand=True)
#for i in range(0,100):
#    lb.insert("end", "item #%s" % i)

#text.pack()
button1.pack()
button2.pack()
#button3.pack()
#listbox.pack()
scrollbar.pack()
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=False)
observer.start()
root.mainloop()
