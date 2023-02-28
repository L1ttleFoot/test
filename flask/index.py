from flask import Flask, jsonify, send_file
import os

absolute_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
relative_path = "tmp"
full_path = os.path.join(absolute_path, relative_path)

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def home():
    response = jsonify('Home Page Route - nice work Andrew!!!')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/about', methods=['GET'])
def about():
    response = jsonify('About Page Route')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    response = jsonify('Portfolio Page Route')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text


@app.route('/get_file')
def get_file():
    f = open('/tmp/const.py', 'w')
    f.write('test')
    f.close()

    return send_file(f'/tmp/const.py', )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
