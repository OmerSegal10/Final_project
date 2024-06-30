from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'super_secret_key')

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'omer2002')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'Sports_db')

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Users (name) VALUES (%s)', (name,))
        mysql.connection.commit()
        session['User_id'] = cursor.lastrowid  
        return redirect(url_for('Football')) 
    return render_template('index.html')

@app.route('/Football', methods=['GET', 'POST'])
def Football():
    if request.method == 'POST':
        try:
            football_team_id = request.form['team']
            session['Football_team_id'] = football_team_id
            return redirect(url_for('Basketball'))
        except KeyError:
            return "Bad Request: Missing 'team' key", 400

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT id, name FROM Teams WHERE type='Football'")
    teams = cursor.fetchall()
    cursor.close()
    return render_template('football.html', teams=teams)

@app.route('/Basketball', methods=['GET', 'POST'])
def Basketball():
    if request.method == 'POST':
        try:
            basketball_team_id = request.form['team']
            user_id = session.get('User_id')
            football_team_id = session.get('Football_team_id')

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO Choices (User_id, Football_team_id, Basketball_team_id) VALUES (%s, %s, %s)', (user_id, football_team_id, basketball_team_id))
            mysql.connection.commit()

            return redirect(url_for('Results'))
        except KeyError:
            return "Bad Request: Missing 'team' key", 400

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT id, name FROM Teams WHERE type = "Basketball"')
    teams = cursor.fetchall()
    cursor.close()

    return render_template('basketball.html', teams=teams)

@app.route('/Results')
def Results():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cursor.execute('SELECT name, COUNT(*) as count FROM Choices JOIN Teams ON Choices.Football_team_id = Teams.id WHERE type = "Football" GROUP BY Football_team_id')
    football_results = cursor.fetchall()

    cursor.execute('SELECT name, COUNT(*) as count FROM Choices JOIN Teams ON Choices.Basketball_team_id = Teams.id WHERE type = "Basketball" GROUP BY Basketball_team_id')
    basketball_results = cursor.fetchall()

    total_football = sum([result['count'] for result in football_results])
    total_basketball = sum([result['count'] for result in basketball_results])

    football_percentages = {result['name']: (result['count'] / total_football) * 100 for result in football_results}
    basketball_percentages = {result['name']: (result['count'] / total_basketball) * 100 for result in basketball_results}

    return render_template('results.html', football_percentages=football_percentages, basketball_percentages=basketball_percentages)

if __name__ == '__main__':
    app.run(debug=True)

