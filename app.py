from flask import Flask, render_template
import json

app = Flask(__name__)

# načtení článků z JSONL souboru
def load_articles():
    articles = []
    with open('articles.jsonl', 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= 100000:  # pro test zobrazíme jen 100 článků
                break
            data = json.loads(line)
            articles.append(data)
    return articles

@app.route('/')
def index():
    articles = load_articles()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:id>')
def article(id):
    articles = load_articles()
    if id < len(articles):
        return render_template('article.html', article=articles[id])
    return "Článek nenalezen", 404

if __name__ == '__main__':
    app.run(debug=True)
