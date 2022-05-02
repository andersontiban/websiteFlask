#Author: Anderson Tiban
#Date: May 2, 2022
#Purpose: Personal website, to display my abities, resume and background.

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", yes = "food")

@app.route('/projects')
def admin():
    github = 'https://github.com/andersontiban'
    return render_template("projects.html", github = github)


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug = True)
