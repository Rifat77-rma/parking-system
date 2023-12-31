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


def Logging_In():
  return render_template('index.html')


def Cancel_Registration():
  return render_template('index.html')





if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
