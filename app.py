from flask import Flask, render_template, request
from helper import mifflin_st_jeor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmr_results', methods=['POST'])
def bmr_results():
    user = [request.form['email'], int(request.form['age']), request.form['weight'], request.form['height'], request.form['gender']]
    bmr = mifflin_st_jeor(user[1], float(user[2]), float(user[3]), user[4])
    user.append(bmr)
    return render_template('bmr_results.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)