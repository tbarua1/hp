import json
from flask import request, Flask, make_response, render_template

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!' + request.path

@app.route('/')
def root():
    return 'Request Path is: ' + request.path

@app.route('/hello1/')
@app.route('/hello1/<fromPagename>')
def hello(fromPagename=None):
    return render_template('hamepage.html', name=fromPagename)


@app.route('/test/')
def test():
    return 'Request Path is ' + request.path


@app.route('/data', methods=['GET'])
def show_data():
    return "i am going to Display Data"


@app.route('/data', methods=['POST'])
def handle_data():
    return "i am going to Handel Data using post"


@app.route('/user/<username>')
def greet_user(username):
    return 'Hello ' + username


@app.route("/json")
def get_image():
    # Create response
    response = make_response(json.dumps({"foo": "bar"}))
    # Set correct mimetype
    response.mimetype = "application/json"
    return response


@app.route("/error")
def error_page():
    response = make_response("Error Page")
    response.status_code = 404
    return response


@app.route("/posts")
@app.route("/posts/page/<int:page_nb>")
def show_posts(page_nb=1):
    first_msg = 1 + 50 * page_nb
    last_msg = first_msg + 49
    return "Messages {} to {}".format(first_msg, last_msg)


if __name__ == '__main__':
    app.run(debug=True)
