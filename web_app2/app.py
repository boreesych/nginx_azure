from flask import Flask


app = Flask(__name__)


@app.route('/')
def my_index_view():
    return 'It is a homepage from app2!'


@app.route('/app2/')
def my_index_view2():
    return 'Hello from the app2!'


if __name__ == '__main__':
    app.run()