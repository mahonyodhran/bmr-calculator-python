from flask import Flask, render_template, request, redirect, url_for
from helper import mifflin_st_jeor, make_message
from database.db_methods import select_all_users, insert_user, delete_user, get_user
from models.user import User

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_user = User(int(request.form['age']),int(request.form['weight']), int(request.form['height']), request.form['gender'] )
        new_user.bmr = mifflin_st_jeor(new_user)
        new_user.email = request.form['email']
        if request.form.get('get_email_check') != None:
            make_message(new_user.email, new_user.bmr)
        insert_user(new_user)
        return render_template('bmr_results.html', new_user=new_user)
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/database_records')
def database_records():
    return render_template('database_records.html', users=select_all_users())

@app.route('/user_delete/<uid>')
def user_delete(uid):
    delete_user(uid)
    return redirect(url_for('database_records'))

if __name__ == "__main__":
    app.run(debug=True)