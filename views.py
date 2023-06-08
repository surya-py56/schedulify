from flask import Flask,render_template,redirect,request
import pymysql as py
app=Flask(__name__)
@app.route('/')
def display():
    try:
        db=py.Connect(host='localhost',user='root',password='',database='todo')
        cur=db.cursor()
        sqq='select * from task'
        cur.execute(sqq)
        data=cur.fetchall()
    except Exception as e:
        print('Error:',e)    
    return render_template('dashboard.html',data=data)

@app.route('/create')
def create():
    return render_template('form.html')

@app.route('/contact')
def contact():
    return render_template('contactus.html')


@app.route('/edit/<rid>')
def edit(rid):
    try:
        db=py.Connect(host='localhost',user='root',password='',database='todo')
        cur=db.cursor()
        sq3="select * from task where id='{}'".format(rid)
        cur.execute(sq3)
        data=cur.fetchall()
        return render_template('editform.html',data=data)
    except Exception as e:
        print('Error',e)
    
        
@app.route('/store',methods=['POST'])
def store():
    t=request.form['title']
    det=request.form['details']
    date=request.form['date']

    try:
        db=py.Connect(host='localhost',user='root',password='',database='todo')
        cur=db.cursor()
        qu='insert into task(title,detail,date) values("{}","{}","{}")'.format(t,det,date)
        cur.execute(qu)
        db.commit()
    except Exception as e:
        print('FAILED to INSERT',e)
    return redirect('/')

@app.route('/update/<rid>',methods=['POST'])
def update(rid):
    t=request.form['title']
    det=request.form['details']
    date=request.form['date']
    try:
        db=py.Connect(host='localhost',user='root',password='',database='todo')
        cur=db.cursor()
        sq2="update task set title='{}',detail='{}',date='{}' WHERE id='{}'".format(t,det,date,rid)
        cur.execute(sq2)
        db.commit()
    except Exception as e:
        print('Failed to update',e)
    return redirect('/')

    
@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=py.Connect(host='localhost',user='root',password='',database='todo')
        cur=db.cursor()
        sq1="delete from task where id='{}'".format(rid)
        cur.execute(sq1)
        data=cur.fetchall()
        db.commit()
        return redirect('/')
    except Exception as e:
        print('Error',e)
    
app.run(debug=True)
