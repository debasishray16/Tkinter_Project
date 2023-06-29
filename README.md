
<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>


# FireBase Construction Application

This Application consists of following CRUD functionality where the data are fetched, deleted, updated and inserted in Firebase Realtime databases.



## Modules

1. [Pyrebase](https://pypi.org/project/Pyrebase/)

2. [Tkinter](https://docs.python.org/3/library/tkinter.html)

## API References

```python
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

```

Then, add this inside your main.py file to establish a connection between your code and Firebase.

```python
firebase = pyrebase.initialize_app(Config)
db = firebase.database()
```
