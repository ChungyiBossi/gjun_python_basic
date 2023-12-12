from flask import Flask, render_template
from web_crawler import get_google_news
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"


@app.route("/google_news/<category_name>")
def crawl_google_news(category_name):
    news = get_google_news(category_name)
    return render_template("google_news.html", google_news=news.items())


if __name__ == "__main__":
    app.run(debug=True)
