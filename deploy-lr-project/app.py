from flask import Flask, render_template, request
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

    if request.method == 'POST':
        # variable = request.form['variable']
        path = "C:/Users/DS_PC/PycharmProjects/irkut2/deploy-lr-project/static/"
        file_old = os.path.join(path, f'{file.filename}')
        file_new = os.path.join(path, "data.csv")
        file = os.rename(file_old, file_new)
        data = pd.read_csv('static/data.csv')  # возможно прийдется взять др. имя - file.filename

        plt.plot(data.loc[0], data.loc[1])
        # sns.pairplot(data, hue=data.loc[0])
        imagepath = os.path.join('static', 'image' + '.png')
        plt.savefig(imagepath)

        if os.path.isfile(path+'data.csv'):
            os.remove(path+'data.csv') # +добавить удаление графика после показа
        return render_template('index.html', image=imagepath)
    return render_template('index.html')
# @app.route('/home', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         request.form
#     path = "C:/Users/DS_PC/PycharmProjects/irkut2/deploy-lr-project/static/"
#     os.remove(path)

if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app
