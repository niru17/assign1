from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/search')
def search():
   return render_template('search.html')

@app.route('/searchstate')
def searchstate():
   return render_template('searchstate.html')
@app.route('/update')
def updatemain():
   return render_template('update.html')


@app.route('/range')
def range():
   return render_template('range.html')





@app.route('/namesearch', methods=['POST','GET'])
def list():
    conn = sqlite3.connect('datan.db')
    cur = conn.cursor()
    field=request.form['name']
    print(field)
    querry="Select * from name WHERE Name =  '"+field+"' "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)

@app.route('/all', methods=['POST','GET'])
def fulllist():
    conn = sqlite3.connect('datan.db')
    cur = conn.cursor()
    querry="Select * from name where Name !='Name'   "
    cur.execute(querry)
    rows = cur.fetchall()
    conn.close()
    return render_template("list.html",rows = rows)


@app.route('/sal', methods=['GET', 'POST'])
def notmatch():
    if (request.method=='POST'):
        conn = sqlite3.connect('datan.db')
        cur = conn.cursor()
        low= str(request.form['low'])
        high= str(request.form['high'])
        print(low, high)
        querry="Select * from name WHERE Num  BETWEEN "+low+" AND "+high+" "
        cur.execute(querry)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)
   


@app.route('/keyupdate',methods=['POST','GET'])
def update():
    if (request.method=='POST'):
        conn = sqlite3.connect('datan.db')
        cur = conn.cursor()
        name= str(request.form['name'])
        keyword= str(request.form['keyword'])
        querry="UPDATE name SET Keywords = '"+keyword+"' WHERE Name ='"+name+"' "
        cur.execute(querry)
        conn.commit()
        querry2="Select * from name WHERE Name =  '"+name+"' "
        cur.execute(querry2)
        rows = cur.fetchall()
        conn.close()
    return render_template("list.html",rows = rows)



 


if __name__ == '__main__':
    app.debug=True
    app.run()
    