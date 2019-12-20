from app import app
from flask import render_template
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

path = './app/static/titanic.csv'
df = pd.read_csv(path)
records = df.head()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/titanic')
def show():
    return render_template('show.html', records=records) 


def build_graph(x_coordinates):
    img = io.BytesIO()
    plt.hist(x_coordinates)
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)

df = df[df['Age'].notnull()]
Age = df.Age


@app.route('/graph')
def graph():
    graph1 = build_graph(Age)
    return render_template('graph.html', graph1=graph1)

