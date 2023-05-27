from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

Hjemmeside = Flask(__name__)

@Hjemmeside.route('/')
@Hjemmeside.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process the login form data
        username = request.form['username']
        password = request.form['password']
        #Vi forbinder os til kodeord_databasen
        con = sql.connect('kodeord_database.db')
        #Vi laver en cursor objekt så vi kan interegere med databasen
        cur = con.cursor()
        query = 'select * from bruger where username=? and password=? and admin=?'
        cur.execute(query, (username, password, 0))
        result = cur.fetchone()
        #Hvis username og password matcher result vil du komme ind på kundesiden
        if result:
            print(result)
            if (result[3]) == "1":
                print("adminside")
                return redirect('/adminside')
            elif (result[3]) == "0":
                print("kundeside")
                return redirect('/kundeside')
            else:
                error = "Invalid username or password"
                flash(error)
    # Render the login HTML template
    return render_template('login.html')

@Hjemmeside.route('/kundeside', methods=['GET', 'POST'])
def kundeside():
    if request.method == 'Get':
        pass
    if request.method == 'POST':
        Involveret = request.form['Involveret']
        Ulykke = request.form['Ulykke']
        Location = request.form['Location']
        print(Involveret,Ulykke,Location)
        con = sql.connect('kundesag.db')
        cur=con.cursor()
        cur.execute('insert into sager(Involveret, Ulykke, Location) values(?,?,?)', (Involveret, Ulykke, Location))
    return render_template('kundeside.html')

@Hjemmeside.route('/adminside', methods = ['GET', 'POST'])
def adminside():
    return render_template('adminside.html')

@Hjemmeside.route('/tilføj_bruger', methods=['GET', 'POST'])
def tilføj_bruger():
    if request.method == 'POST':    
        username = request.form['username']
        password = request.form['password']
        admin = request.form['admin']
        print(username,password, admin)
        con=sql.connect("kodeord_database.db")
        cur=con.cursor()
        cur.execute("insert into bruger(username,password,admin) values (?,?,?)",(username,password,admin))
        con.commit()
        flash('user added', 'success')
        return redirect('/login')
    return render_template("tilføj_bruger.html")



if __name__ == '__main__':
    Hjemmeside.secret_key = 'SECRET_KEY'
    Hjemmeside.run(debug=True)
