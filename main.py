from tkinter import *
from tkinter import messagebox
import pyrebase


root = Tk()
root.geometry("500x500")
root.title("First Screen")

# Required to connect to firebase realtime database
Config = {
    "apiKey": "AIzaSyB3b7J7D5LHOqrhdvAfOivEHdUhj23_73s",
    "authDomain": "python-a4ee7.firebaseapp.com",
    "databaseURL": "https://python-a4ee7-default-rtdb.firebaseio.com",
    "projectId": "python-a4ee7",
    "storageBucket": "python-a4ee7.appspot.com",
    "messagingSenderId": "666918671924",
    "appId": "1:666918671924:web:d98ddefa593c64c2b95c61",
    "measurementId": "G-WFM6B52WE0"
}


firebase = pyrebase.initialize_app(Config)
db = firebase.database()


def getvals():

    # Get values
    namevalue = nameentry.get()
    phonevalue = phoneentry.get()
    gendervalue = genderentry.get()
    emergencyvalue = emergencyentry.get()
    paymentvalue = paymentmodeentry.get()

    # Created a dictionary to store data sequencely.
    getval = {"name": namevalue, "Phone": phonevalue, "Gender": gendervalue,"Emergency": emergencyvalue, "Payment Method": paymentvalue}

    # Used to put the name as the first name to particular table.
    db.child("user").push(getval)

    messagebox.showinfo("Info", "Data Stored")


Label(root, text="Python Registration Form",font="arial 15 bold").grid(row=0, column=3)


name = Label(root, text="Name").grid(row=1, column=2)
phone = Label(root, text="Phone Number").grid(row=2, column=2)
gender = Label(root, text="Gender").grid(row=3, column=2)
emergency = Label(root, text="Emergency").grid(row=4, column=2)
paymentmode = Label(root, text="Payment Method").grid(row=5, column=2)


namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()
checkvalue = IntVar()


nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
paymentmodeentry = Entry(root, textvariable=paymentmode)
emergencyentry = Entry(root, textvariable=emergencyvalue)


nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
paymentmodeentry.grid(row=4, column=3)
emergencyentry.grid(row=5, column=3)


checkbtn = Checkbutton(text="Remember Me?",variable=checkvalue).grid(row=6, column=3)
Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()
