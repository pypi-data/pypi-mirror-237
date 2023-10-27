yav is a minimalist python package management tool built on top of venv. 

## Installation

```bash
pip install yav
```
## Usage

If you haven't created a venv folder 
```bash
yav init #  This will create venv and a requirements.txt file
```

After you have set up venv using yav or native methods   

````bash

yav add <package> # Using pip from venv to intall a new package and update requirements.txt

yav remove <package> # Using pip from venv to uninstall a package and update requirements.txt

yav run <*.py> # Using venv to run a python file

```
