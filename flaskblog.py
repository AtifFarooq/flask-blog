from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '87f44fb92f5e930fb0c96499d46a616b'

posts = [
    {
        'author': 'Atif Farooq',
        'title': 'First Blog Post',
        'content': 'Lorep Ipsum etc.',
        'data_posted': 'November 19, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second Blog Post',
        'content': 'Second post content',
        'data_posted': 'November 21, 2018'
    },


]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)
