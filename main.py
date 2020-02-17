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

@app.route('/', methods=['GET', 'POST'])
def login():
	return render_template('index.html', msg='')


@app.route('/tables', methods=['GET', 'POST'])
def tables():
	return render_template('tables.html', msg='')

@app.route('/1', methods=['GET', 'POST'])
def one():
	return render_template('1.html', msg='')	

@app.route('/2', methods=['GET', 'POST'])
def two():
	return render_template('2.html', msg='')		

@app.route('/3', methods=['GET', 'POST'])
def three():
	return render_template('3.html', msg='')		

if __name__ == "__main__":
  app.run(static_folder='static')
  #serve(app)
