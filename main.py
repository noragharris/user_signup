from flask import Flask, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods = ['POST'])
    return render_template('base.html')

app.run()