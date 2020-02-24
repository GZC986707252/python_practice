from flask import Flask,request,render_template
import flask

app = Flask(__name__,template_folder='templates/')

@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def Login():
    msg=[]
    data={}
    user={}
    if request.method == 'POST':
        user['name']=request.form['name']
        user['password']=request.form['password']
        data['status']='登录成功！'
        data['user']=user
        msg.append(data)
        print(msg)
        return render_template('success.html',msg=msg)   
    else:
        return render_template('index.html')