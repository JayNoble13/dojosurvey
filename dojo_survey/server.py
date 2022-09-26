from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '1q2w3e4r'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process_form', methods=['POST'])
def process_form():
    session['first']=request.form['first_name']
    session['last']= request.form['last_name']
    session['local']= request.form['location']
    session['lang']= request.form['language']
    session['comments']= request.form['comments']
    return redirect('/results')

@app.route('/results')
def showuser():
    return render_template('results.html', first= session['first'], last= session['last'],location= session['local'], character= session['lang'], favorite= session['comments'])

if __name__=="__main__":
    app.run(debug=True)