### Flask [A simple web based exploration repository]
#### MPOP Reverse II (Ryann Kim Sesgundo)

---
### Introduction
> `Flask` for me is a type of python package, which is a good alternative for `Django`. This package looks like Laravel but easier to use and to setup.

---
### Packages
> Please read the [#Installation](Installation) first, before you proceed.

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