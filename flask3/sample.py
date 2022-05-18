from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
import numpy as np
from controller.posts_controller import name_check1,name_check2,name_reverse,name_duplicate

app = Flask(__name__)


app.errorhandler(Exception)
def exception_handler(e):
    return "handling exception"

from werkzeug.exceptions import NotFound
bp = Blueprint('exception', __name__)
bp.errorhandler(NotFound)
def bp_notfound(e):
    return "handling NotFound"


def picked_up():
    messages = [
        "あなたの名前を入力してください",
        "お名前を代入して下さい",
        "お名前を教えて下さい"
    ]
    return np.random.choice(messages)

@app.route('/')
def index():
    title = "課題"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "課題"
    error = None

    if request.method == 'POST':
        firstname = str(request.form['firstname'])
        lastname = str(request.form['lastname'])

        firstname1 = name_check1(firstname)
        lastname1 = name_check1(lastname)
        firstname2 = name_check2(firstname)
        lastname2 = name_check2(lastname)

        if firstname1 and lastname1 and firstname2 and lastname2:

            lastname = name_reverse(lastname)
            firstname = name_duplicate(firstname)
            error = None
            return render_template('index.html',
                                firstname=firstname,lastname=lastname ,title=title,error=error)

        elif firstname1 == False:
            lastname = name_reverse(lastname)
            error = '名前を全角文字で入力して下さい'
            return render_template('index.html',
                                firstname="  ",lastname=lastname ,title=title,error=error)
        elif lastname1 ==  False:
            firstname = name_duplicate(firstname)
            error = '苗字を全角文字で入力して下さい'
            return render_template('index.html',
                                firstname=firstname,lastname="  " ,title=title,error=error)
        elif firstname2 ==  False:
            lastname = name_reverse(lastname)
            error = '名前を16文字以下で入力して下さい'
            return render_template('index.html',
                                firstname="  ",lastname=lastname ,title=title,error=error)
        elif lastname2 ==  False:
            firstname = name_duplicate(firstname)
            error = '苗字を16文字以下で入力して下さい'
            return render_template('index.html',
                                firstname=firstname,lastname="  " ,title=title,error=error)

    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')