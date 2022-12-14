from flask import Flask, jsonify
import os

absolute_path = os.path.dirname(__file__)
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

@app.route('/api2')
def api():
    f=open(f'{full_path}/const_new.py','w')
    f.write('test')
    f.close()



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
