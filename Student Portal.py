from tabnanny import check
from tkinter import *
from tkinter import ttk

mainWindow = Tk()
newWindow = None
_row = None

def addStudentToDB(name, id, course, fieldId, fieldNama):
    global _row
    f = open("students.txt", "a")
    f2 = open("students.txt", "r")
    if f2.readlines is None:
        data = f"{name},{id},{course}"
    else:
        data = f"\n{name},{id},{course}"
    f.write(data)
    _col = 0
    for word in data.split(","): 
                field = Entry(newWindow)
                field.grid(column=_col, row=_row+1)
                field.insert(0, word)
                _col += 1
    _row += 1
    fieldId.delete(0,END)
    fieldNama.delete(0,END)
    f.close()
    f2.close()

def addNewStudent():
    newWindow = Toplevel(mainWindow)
    newWindow.title("Add Student")

    id = StringVar()
    name = StringVar()
    course = StringVar()

    fieldID = Entry(newWindow, textvariable = id)
    fieldNama = Entry(newWindow, textvariable = name)

    courseOptions = ["Information System", "Computer Science", "Art"]
    fieldCourse = OptionMenu(newWindow , course , *courseOptions )
    course.set(courseOptions[0])

    Label(newWindow, text="           ").grid(column=0, row=0)
    Label(newWindow, text="Tambah Student").grid(column=1, row=0)
    Label(newWindow, text="           ").grid(column=2, row=0)

    Label(newWindow, text="Nama : ").grid(column=0, row=1)
    fieldID.grid(column=1, row=1)
    Label(newWindow, text="ID : ").grid(column=0, row=2)
    fieldNama.grid(column=1, row=2)
    Label(newWindow, text="Course : ").grid(column=0, row=3)
    fieldCourse.grid(column=1, row=3)
    Label(newWindow, text="           ").grid(column=1, row=4)
    Button(newWindow, text="Add New student", command=lambda: addStudentToDB(fieldNama.get(), fieldID.get(), course.get(), fieldID, fieldNama)).grid(column=1, row=5)

def checkForNewStudent(window, currStudentCount):
    newCount = 0
    
    with open("students.txt","r") as f:
        allStudents = f.readlines()
        print("Checking for new student")
        print(allStudents)
        newCount = len(allStudents)
    
    line = allStudents[newCount-1]
    _col = 0
    if currStudentCount != newCount:
        print("New Student found!")
        for word in line.split(","): 
                field = Entry(window)
                field.grid(column=_col, row=newCount)
                field.insert(0, word)
                _col += 1

def viewStudents():
    global newWindow
    newWindow = Toplevel(mainWindow)
    newWindow.title("All Students")
    newWindow.geometry("1200x600")
    global _row
    _row = 0
    _col = 0
    with open("students.txt","r") as f: 
        for line in f:
            for word in line.split(","): 
                field = Entry(newWindow)
                field.grid(column=_col, row=_row)
                field.insert(0, word)
                _col += 1
            _col = 0
            _row += 1
    # newWindow.after(100, lambda: checkForNewStudent(newWindow, _row))
    # Button(newWindow, text="Delete last student", command=lambda: refreshWindow(newWindow)).grid(column=1, row=_row+1)

def main():
    global mainWindow
    mainWindow.option_add( "*font", "lucida 25" )
    Label(mainWindow, text="           ").grid(column=0, row=0)
    Label(mainWindow, text="Student Portal").grid(column=1, row=0)
    Label(mainWindow, text="           ").grid(column=2, row=0)
    Button(mainWindow, text="View all Students", command=viewStudents).grid(column=1, row=1)
    Button(mainWindow, text="Add New student", command=addNewStudent).grid(column=1, row=2)
    mainWindow.mainloop()

if __name__ == "__main__":
    main()