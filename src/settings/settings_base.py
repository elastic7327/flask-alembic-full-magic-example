import os
import sqlite3
from flask import Flask

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = os.path.join(BASE_DIR, '../../databases/db.sqlite3'),
DEBUG = True
SECRET_KEY = 'AMNAS@#(@#9===ASKDj)KAS=/ASDKK(@(#KDASDJKAAAL)@(I@#U))'

USERNAME = 'admin'
PASSWORD = 'incorrect'

app = Flask(__name__)
app.config.from_object(__name__)
