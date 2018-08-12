# Flask Website Setup Guide #
# ========================================= #

# Author: Cher Don Liew
# Date of Modification: 12.08.2018
# Description: Using Flask Framework to set up a database for login on a website
# Keywords: Flask, Python
# Usage: This Python File initialises the Flask class into the variable "app".

# ----------------------------------------- #

from flask import Flask

app = Flask(__name__)
from app import views
