<<<<<<< HEAD
from flask import Flask, request, render_template, session

=======
from flask import flask, request, render_template, session
from flask_socketio import SocketIO, emit, join_room
>>>>>>> parent of 9fb367e... qwq

class Userinfo:
    def __init__(self, id, nickname, permission):
        self.id = id
        self.nickname = nickname
        self.permission = permission

    



app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def main():
    if request.method == 'POST':
        return '<h1>POST SUCCESS</h1>'
        
    return render_template('main.html')

@app.route('/login', methods = ['GET','POST'])
def post_login():
    pass

@app.route('/<category>/post')
def category_post():
    pass

if __name__ == '__main__':
    app.run(host = '203.252.231.149', port = 5000, debug = True)

    print("1")