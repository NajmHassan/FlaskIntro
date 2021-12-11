from flask import Flask, render_template,flash
from create_fake_users import create_fake_users
app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'
users = create_fake_users(105)
@app.route('/')
def home():
   return render_template('nav.html')

@app.route('/calculate/')
def calc():
   flash("flash TEST!!!")
   return render_template('calc.html')

@app.route('/table/')
def index():
    return render_template('bootstrap_table.html', title='Bootstrap Table',
                           users=users)

if __name__ == '__main__':
   app.run()