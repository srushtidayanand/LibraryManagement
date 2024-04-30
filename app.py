from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


conn.execute('''CREATE TABLE IF NOT EXISTS books
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                title TEXT, 
                author TEXT, 
                year INTEGER)''')
@app.route('/')
def home():
    # Fetch all books from the database
    with sqlite3.connect('library.db') as conn:
        books = conn.execute('SELECT * FROM books').fetchall()
    return render_template('lib.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    year = int(request.form['year'])
    with sqlite3.connect('library.db') as conn:
        conn.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
    return 'Book added successfully!'

@app.route('/update', methods=['POST'])
def update_book():
    book_id = int(request.form['id'])
    title = request.form['title']
    author = request.form['author']
    year = int(request.form['year'])
    with sqlite3.connect('library.db') as conn:
        conn.execute('UPDATE books SET title = ?, author = ?, year = ? WHERE id = ?', (title, author, year, book_id))
    return 'Book updated successfully!'

@app.route('/delete', methods=['POST'])
def delete_book():
    book_id = int(request.form['id'])
    with sqlite3.connect('library.db') as conn:
        conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
    return 'Book deleted successfully!'

@app.route('/search', methods=['GET'])
def search_books():
    search_query = request.args.get('query', '')
    with sqlite3.connect('library.db') as conn:
        results = conn.execute('SELECT * FROM books WHERE title LIKE ? OR author LIKE ?', (f'%{search_query}%', f'%{search_query}%')).fetchall()
    return jsonify(results)



