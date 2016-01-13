#-*- coding: iso-8859-1 -*-

from Tkinter import *
import os
import fileinput
import sys

def make_todo_list_dict(goal_entry, entry_name, button_make_new_todo_list_dict, frame_origin, newly_made):
	goal = goal_entry.get()
	button_make_new_todo_list_dict.destroy()
	button_add_new_values = Button(frame_origin, text="Add new values",
										command=lambda: add_new_values(goal, entry_name,
										 number_of_labels, t, button_make_new_todo_list_dict, frame_origin, 
										 goal_entry, button_delete_just_added=None, first_time=True))
	button_add_new_values.pack()
	t = Toplevel(root)
	t.minsize(200, 5)
	t.wm_title("Time to " + goal +"!")
	t.geometry('+260+150') 
	status = Label(t, text="© 2015 Danny Cairns", bg="white", bd=1, relief=SUNKEN, anchor=W)
	status.pack(side=BOTTOM, fill=X)
	frame = Frame (t)
	frame.pack()
	list = ["My goal is to " + goal +" \n and to get there I must first complete these tasks:"]
	items_todo_raw = entry_name.get()
	clean_items = items_todo_raw.split(",")
	just_added = len(clean_items)
	number_of_labels = 0
	label1 = Label(frame, text=list[0])
	label1.pack()
	for i in range(0, len(clean_items)):
		list.append('Task #' + str(i+1) + ") " + clean_items[i])
	for item in list[len(list)-just_added:len(list)]:
		label = Label(frame, text=item)
		label.pack()
		number_of_labels += 1
	button_delete_this_list = Button(frame, text="Delete this list", 
		command=lambda: delete_these_values(goal_entry, entry_name, number_of_labels, 
											button_add_new_values, list, just_added, frame, frame_origin,
											 t, newly_made=True))
	button_delete_this_list.pack()

def add_new_values(goal, entry_name, number_of_labels, t, button_add_new_values, frame_origin, goal_entry, 
										button_delete_just_added, first_time):
	button_add_new_values.destroy()
	
	frame = Frame (t)
	frame.pack()
	list = ["My goal is to " + goal +" \n and to get there I must first complete these tasks:"]
	items_todo_raw = entry_name.get()
	clean_items = items_todo_raw.split(",")
	just_added = len(clean_items)
	for i in range(0, len(clean_items)):
		list.append('Task #' + str(i+number_of_labels+1) + ") " + clean_items[i])
	for item in list[len(list)-just_added:len(list)]:
		label = Label(frame, text=item)
		label.pack()
		number_of_labels += 1
	if first_time:
		button_delete_just_added = Button(frame, text="Delete the values just added",
			 										command=lambda: delete_these_values(goal_entry, entry_name, 
			 											number_of_labels, button_delete_just_added, list, just_added, frame,
			 											 frame_origin, t, newly_made=False))
		button_delete_just_added.pack()
	else:
		pass
def make_todo_list_first(goal):
	frame_origin = Frame(root)
	frame_origin.pack(side=RIGHT)
	label_name = Label(frame_origin, text="Enter your todo items separated by commas")
	label_name.pack()
	entry_name = Entry(frame_origin)
	entry_name.pack()
	button_make_new_todo_list_dict = Button(frame_origin, text="Start your list", 
												command=lambda: make_todo_list_dict(goal, entry_name, 
													button_make_new_todo_list_dict,
												 frame_origin, newly_made=True))
	button_make_new_todo_list_dict.pack()

def delete_these_values(goal_entry, entry_name, number_of_labels, button_delete_this_list, 
						list, just_added, frame, frame_origin, t, newly_made):
	if newly_made:	
		button_delete_this_list.destroy()
		button_make_new_todo_list_dict = Button(frame_origin, text="Start your list", 
														command=lambda: make_todo_list_dict(goal_entry,
														 entry_name, button_make_new_todo_list_dict, frame_origin, newly_made=True))
		##the problem here is that goal is already get()ed by this time, so when a new list is made it's all wonky...
		button_make_new_todo_list_dict.pack()
		list[-1:-1-(just_added)] = []
		t.destroy()
	else:
		list[-1:-1-(just_added)] = []
		frame.destroy()

def _quit(event):
    root.destroy()


root = Tk()
root.geometry('+650+150')
root.wm_title("todo list")	
root.minsize(250, 5)
status = Label(root, text="© 2015 Danny Cairns", bg="white", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
frame = Frame(root)
frame.pack()
label_name = Label(frame, text="Enter your goal")
label_name.pack()
entry_name = Entry(frame)
entry_name.pack()

button_make_new_todo_list_first = Button(frame, text="Let's make a todo list!", command=lambda: make_todo_list_first(entry_name))
button_make_new_todo_list_first.pack()
root.bind('<Control-Q>', _quit)
root.bind('<Control-q>', _quit)
root.mainloop()
###looks like I have to relocate the button to after the entry or else the entry enters undefined...a project for another time.

