from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bmr_results', methods=['POST'])
def bmr_results():
    user = [request.form['email'], request.form['age'], request.form['weight'], request.form['height'], request.form['gender']]
    return render_template('bmr_results.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)