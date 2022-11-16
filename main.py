from flask import Flask
from flask import send_from_directory
from flask import render_template
from flask import make_response

app = Flask(__name__)


FLUTTER_WEB_APP = 'templates'

@app.route('/')
def render_page():
    return render_template('index.html')




@app.route('/firebase-messaging-sw.js')
def sw():
    response=make_response(
                     send_from_directory('static','firebase-messaging-sw.js'))
    #change the content header file. Can also omit; flask will handle correctly.
    response.headers['Content-Type'] = 'application/javascript'
    return response


@app.route('/<path:name>')
def return_flutter_doc(name):

    datalist = str(name).split('/')
    DIR_NAME = FLUTTER_WEB_APP

    if len(datalist) > 1:
        for i in range(0, len(datalist) - 1):
            DIR_NAME += '/' + datalist[i]
    return send_from_directory(DIR_NAME, datalist[-1])



if __name__ == '__main__':
    app.run()