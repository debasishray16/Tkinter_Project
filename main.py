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
    name_value = name_entry.get()
    phone_value = phone_entry.get()
    gender_value = gender_entry.get()
    emergency_value = emergency_entry.get()
    payment_value = paymentmode_entry.get()

    # Created a dictionary to store data sequencely.
    getval = {"name": name_value, "Phone": phone_value, "Gender": gender_value,"Emergency": emergency_value, "Payment Method": payment_value}

    # Used to put the name as the first name to particular table.
    db.child("user").push(getval)

    messagebox.showinfo("Info", "Data Stored")


Label(root, text="Python Registration Form",font="arial 15 bold").grid(row=0, column=3)


name = Label(root, text="Name").grid(row=1, column=2)
phone = Label(root, text="Phone Number").grid(row=2, column=2)
gender = Label(root, text="Gender").grid(row=3, column=2)
emergency = Label(root, text="Emergency").grid(row=4, column=2)
paymentmode = Label(root, text="Payment Method").grid(row=5, column=2)


name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
emergency_value = StringVar()
payment_value = StringVar()
check_value = IntVar()


name_entry = Entry(root, textvariable=name_value)
phone_entry = Entry(root, textvariable=phone_value)
gender_entry = Entry(root, textvariable=gender_value)
paymentmode_entry = Entry(root, textvariable=payment_value)
emergency_entry = Entry(root, textvariable=emergency_value)


name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
paymentmode_entry.grid(row=4, column=3)
emergency_entry.grid(row=5, column=3)


checkbtn = Checkbutton(text="Remember Me?",variable=check_value).grid(row=6, column=3)
Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()
