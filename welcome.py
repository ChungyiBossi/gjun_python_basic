from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/works")
def hello_works():
    articles = list()
    for i in range(10):
        articles.append({
            'image_path': "static/MC.jpg",
            "project_name": f"Project {i}",
            'project_description': f"This is project {i}"
        })
    return render_template('webpage.html', articles=articles)