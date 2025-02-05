from flask import Flask,render_template,request,url_for,redirect
import mysql.connector

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="yoga"
    )
    if request.method == 'POST':
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        date=request.form.get('date')
        email=request.form.get('email')
        phone=request.form.get('number')
        selecct=request.form.get('gender')
        message=request.form.get('msg')
        mycursor=mydb.cursor()
        sql="INSERT INTO user(fname,lname,monthnddate,classs,phone,email,msg) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        val=(fname,lname,date,selecct,phone,email,message)
        mycursor.execute(sql,val)
        mydb.commit()
        return redirect(url_for('home'))
    return render_template('index.html',Titlte='Home')

if __name__ == '__main__':
    app.run(debug=True)