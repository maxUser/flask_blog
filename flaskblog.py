from flask import Flask, render_template, url_for
app = Flask(__name__)

# list of dictionaries
# each dictionary is a blog post
posts = [
    {
        'author': 'Max Kasprzik',
        'title': 'Blog post 1',
        'content': 'whateva u want',
        'date_posted': 'April 20, 2018',
    },
    {
        'author': 'Michael Kasprzik',
        'title': 'Blog post 2',
        'content': 'gotcha!',
        'date_posted': 'April 21, 2018',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
