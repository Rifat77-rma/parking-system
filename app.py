from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')


@app.route('/ratings')
def ratings():
  return render_template('ratings.html')


@app.route('/register')
def register():
  return render_template('register.html')


if __name__ == '__main__':
  app.run(debug=True)
