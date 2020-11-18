from flask import request, redirect, url_for, render_template, flash, session
from flask_contents import app

# app.jinja_loader = FileSystemLoader("templates/entries")
@app.route('/')
def show_index():
    return render_template('entries/index.html')

@app.route('/url')
def show_url():
    return render_template("entries/url.html")

@app.route('/go', methods=["POST"])
def show_test():
    return render_template('entries/test.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.form['password'] != app.config['PASSWORD']:
        flash('パスワードが異なります')
    else:
        session['logged_in'] = True
        flash('ログインしました')
        return redirect(url_for('test.html'))
    return render_template('login.html')
