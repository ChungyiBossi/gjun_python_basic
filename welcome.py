from flask import Flask
from flask import render_template
from web_crawler import get_google_news

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/news/<category>")
def hello_news(category):
    # articles = list()
    # for i in range(10):
    #     articles.append({
    #         'image_path': "static/MC.jpg",
    #         "project_name": f"Project {i}",
    #         'project_description': f"This is project {i}"
    #     })

    news = get_google_news(category)
    print(len(news))
    return render_template('webpage.html', articles=news.items())