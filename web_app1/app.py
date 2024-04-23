from flask import Flask


app = Flask(__name__)


@app.route('/')
def my_index_view():
    return 'It is a homepage!'


@app.route('/app1/')
def my_index_view2():
    return 'Hello from the app1!'


if __name__ == '__main__':
    app.run()