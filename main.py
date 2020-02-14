from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
from waitress import serve
import MySQLdb.cursors
import re


app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = '192.168.0.250'
app.config['MYSQL_USER'] = 'cron'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'asterisk'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
	return render_template('dashboard.html', msg='')


@app.route('/pythonlogin/tables', methods=['GET', 'POST'])
def tables():
	return render_template('tables.html', msg='')

@app.route('/pythonlogin/icons', methods=['GET', 'POST'])
def icons():
	return render_template('icons.html', msg='')	

if __name__ == "__main__":
  #app.run()
  serve(app)