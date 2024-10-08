from flask import Flask, request, jsonify, render_template
from helper import recommend_books

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        query_params = {
            'name': request.form.get('name'),
            'authors': request.form.get('authors'),
            'publish_year': request.form.get('publish_year'),
            'publisher': request.form.get('publisher')
        }
        recommendations = recommend_books(query_params)
        return render_template('results.html', recommendations=recommendations)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
