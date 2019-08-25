import pandas as pd
from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def csv_upload():
    csvfile = request.files.get('csvfile')
    df = pd.read_csv(csvfile.stream)
    return df.to_string()

if __name__ == '__main__':
    app.run()
