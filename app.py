from flask import Flask, render_template,flash
app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'

@app.route('/')
def home():
   return render_template('nav.html')

@app.route('/calculate/')
def calc():
   flash("flash TEST!!!")
   return render_template('calc.html')

if __name__ == '__main__':
   app.run()