#Flask Tutorial 1

from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Muhda Chachni',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted':'April 21, 2022'
    },
    {
        'author': 'Muhda Chachni',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted':'April 22, 2022'
    }

]


#Main Route Index 
@app.route("/")
@app.route("/home")
def home():
    #return "Hello! this is the main page <h1>Testtttts?</h1>"
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    #return "Hello! this is the about page <h1>TeSs?</h1>"
    return render_template('about.html', title="About")


if __name__ == "__main__":
    app.run(debug=True)