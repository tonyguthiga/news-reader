from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to News-reader website for the best preview of news articles'
    return render_template('index.html',title = title)

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View news page function that returns the news details page and its data
    '''
    title = 'Home - News ID '
    return render_template('news.html',title = title)