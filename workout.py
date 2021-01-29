import sqlite3
import sys
import os
import tkinter as tk
from typing import Text
os.system("clear")



conn = sqlite3.connect('workout_data.db')
c = conn.cursor()

# c.execute("""CREATE TABLE workouts (
#             date text,
#             workouttype text,
#             workoutinfo text
#             )""")

def insert_data():
    with conn:
        c.execute("INSERT INTO workouts VALUES ('{}', '{}', '{}')".format(date, workoutTitle, workoutInfo))

def get_workouts_by_date(date):
    
    c.execute("SELECT * FROM workouts WHERE date= :date", {'date': date})
    return c.fetchall()

def show_all_workouts():
    with conn:
        c.execute("SELECT * FROM workouts")
        print(c.fetchall())

root = tk.Tk()

# canvas = tk.Canvas(width=100, height=200)
# canvas.grid()

label1 = tk.Label(root, text='Hello')
label1.grid(row=1, column=0)

label2 = tk.Label(root, text='Hello')
label2.grid(row=2, column=0)

label3 = tk.Label(root, text='Hello')
label3.grid(row=3, column=0)

label4 = tk.Label(root, text='Hello')
label4.grid(row=4, column=0)

entry1 = tk.Entry(root)
entry1.grid(row=1, column=1)

entry2 = tk.Entry(root)
entry2.grid(row=2, column=1)

entry3 = tk.Entry(root)
entry3.grid(row=3, column=1)

entry4 = tk.Entry(root)
entry4.grid(row=4, column=1)



root.mainloop()


# addOrClose = input("What would you like to do:\n(0) Exit\n(1) Enter a new workout\n(2) Show all workouts\n(3) Search workouts by date\n\n")



# if(addOrClose == '0'):
#     sys.exit(0)  

# elif(addOrClose == '1'):
#     date = input("What is today's date (MM/DD/YYYY: ")
#     workoutTitle = input("What was the workout: ")
#     workoutInfo = input("What did you do during the workout: ")   
#     insert_data()

# elif(addOrClose == '2'):
#     show_all_workouts()


# elif(addOrClose =='3'):
#     search = input("Search date: ")
#     searchDate = get_workouts_by_date(search)
#     print(searchDate)
#     pass

    



c.close()
