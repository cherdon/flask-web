# Flask Website Setup Guide #
# ========================================= #

# Author: Cher Don Liew
# Date of Modification: 12.08.2018
# Description: Using Flask Framework to set up a database for login on a website
# Keywords: Flask, Python
# Usage: This Python File decorates the function with the mapped URLs

# ----------------------------------------- #

from app import app

@app.route('/')
def test():
    return "This is the first website?"

@app.route('/index')
def index():
    return "Hello, World!"
