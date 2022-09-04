
from flask import Flask,render_template,request,jsonify,session,redirect
from flask_socketio import SocketIO,send

app = Flask(__name__)
app.secret_key = "harri07"
socketio = SocketIO(app,cors_allowed_origins = "*")

@socketio.on('mye')
def handle(message):
    
    send(message,broadcast = True)

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('home.html')


@app.route('/setuser', methods = ['POST'])
def setuser():
    r = request.form['user']
    session['user'] = r 

    return jsonify({'data' :  1})


@app.route('/getuser', methods = ['POST'])
def getuser():
    d = session['user']
    print(d)
    return jsonify({'data' : d})

@app.route('/home', methods = ['POST','GET'])
def home():
    try:
        print(session['user'])
        if session['user']:
            return render_template('index.html')
        else:
            return redirect('/')
    except:
        return redirect('/')
