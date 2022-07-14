from flask import Flask, render_template, request
import os
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

app = Flask(__name__)  # create an app instance


@app.route('/', methods=['GET', 'POST'])  # at the end point /
def index():
    if request.method == 'POST':
        file = request.files['csvfile']
        if not os.path.isdir('static'):
            os.mkdir('static')
        filepath = os.path.join('static', file.filename)
        file.save(filepath)
        return 'The file name of the uploaded file is: {}'.format(file.filename)
    return render_template('index.html')


@app.route('/dash', methods=['GET', 'POST'])
def dash():
    if request.method == 'POST':
        variable = request.form['variable']
        file_old = os.path.join("C:/Users/DS_PC/PycharmProjects/irkut2/deploy-lr-project/static/", "data.csv")
        file_new = os.path.join("C:/Users/DS_PC/PycharmProjects/irkut2/deploy-lr-project/static/", "datas.csv")
        file = os.rename(file_old, file_new)
        # print(file.name)
        print('------------------------------------------------')
        data = pd.read_csv('static/datas.csv')  # возможно прийдется взять др. имя - file.filename
        plt.plot(data[variable])
        imagepath = os.path.join('static', 'image' + '.png')
        plt.savefig(imagepath)
        return render_template('image.html', image=imagepath)
    return render_template('dash.html')


if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app
