### Flask [A simple web based exploration repository]
#### MPOP Reverse II (Ryann Kim Sesgundo)

---
### Introduction
> `Flask` for me is a type of python package, which is a good alternative for `Django`. This package looks like Laravel but easier to use and to setup.

---
### Packages
> Please read the [Installation](#installation) first, before you proceed.

1. Virtual Environment
```Bash
pip install virtualenv
```

2. Flask
``` Bash
pip install flask
```

---
### Installation
> There are primary things which are very required to do, you need to have `virtual environment` before you have these packages. Then you also need to initiate and activate the virtualenv first, before you install flask. To start execute `pip install virtualenv` then `virtualenv venv`.  Next is you need to activate by executing `.\venv\Script\activate` for windows. And lastly, you need to install it thru `pip install flask`

---
### Start my app
> First thing you need to know, is to build a simple webpage here, but first, you need to create a Folder just same as the directory shown below.
```
+ Flask Project
+- ProjectBase
+- venv
```
> The `ProjectBase is the app name i'm using. meaning to say, this is the folder where I add all my resources inside of my flask project. next is you need to create a file inside of your folder, example is main.py.
```
+ Flask Project
+- ProjectBase
  +- main.py
+- venv
```

> Inside of your file add this simple code
``` Python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "<h1>Hello</h1>"
```
> In this format, you'll see a html code, inside of your python which can be seen as like as the webpage.

---
### How to run
> So basically, you need to execute to your terminal like this:
``` Bash
flask --app ProjectBase/main run
```
> Where ProjectBase is our folder and main is our index or file name or the main program.

---
### How to add templates
> So basically, we need to create a folder called `templates` aligned with our main.py or the main python file.
```
+ Flask Project
+- ProjectBase
  +- main.py
  +- templates
	+- index.html
+- venv
```
---
### How to use templates
> To use it, we need ot use the `render_template` from flask package. We will going to return a function with a render template, so that we may call the `html` inside of template.
``` Python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_templates("index.html")
```
---
### How to add static files
> We all know that use of static files, is to store some external files such as images, styles and scripts to our project. To start, we need to create a static folder aligned with `main.py` and `templates`.

```
+ Flask Project
+- ProjectBase
  +- main.py
  +- static
	+- img
		+- sample.jpg
	+- styles.css
	+- script.js
  +- templates
	+- index.html
+- venv
```

> The tree above, is just an illustration for you to understand more about this, This may help you to uniform and make your workplace better. To call this, just simply setup `static_url_path="/static"` inside of the Flask and do like this sample in your html code:

**main.py**
``` Python
from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")	

@app.route("/")
def index():
	return render_template("index.html")
```

**Styles**
``` HTML
<!DOCTYPE html>
<html>
	<head>
		<link href="/static/styles.css">
	</head>
</html>
```
**Script**
``` HTML
<!DOCTYPE html>
<html>
	<script src="/static/styles.css"></script>
</html>
```
**Images**
``` HTML
<!DOCTYPE html>
<html>
	<body>
		<img src="/static/img/sample.jpg">
	</body>
</html>
```

---
### How to setup with SQLite3
> Since SQLite is a default in python 2.x or auto installed, you don't need to install it manually. So first, you need to connect to your sqlite database file and create a table like this code:
``` Python
import sqlite3

con = sqlite3.connect("db.sqlite", check_same_thread=False) # To connect, check same thread is used for you to delete some files
cur = con.cursor() # I forgot the use, but maybe the conenction between sqlite connection and your query

cur.execute("""CREATE TABLE IF NOT EXISTS users (
	'ID' INTEGER PRIMARY KEY NOT NULL, 
	'usn' TEXT, 
	'pass' TEXT
)""") # Execution

con.commit() # This is to save as file
```

> With the help of these code, with comments, you can see now the use of different functions as basics. The `.execute()` is a useful function, for you to communicate with your SQLite file. For more details about [SQL Queries Basics kindly follow ths link](https://github.com/RyannKim327/SQL-Samples).