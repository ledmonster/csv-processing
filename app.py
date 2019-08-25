import pandas as pd
from flask import Flask, render_template, Response
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def csv_upload():
    csvfile = request.files.get('csvfile')
    df = pd.read_csv(csvfile.stream, index_col="index")
    df["row4"] = df["row3"]*2
    res = Response(df.to_csv(), mimetype="application/octet-stream")
    res.headers['Content-Disposition'] = u'attachment; filename=processed.csv'
    return res


if __name__ == '__main__':
    app.run()
