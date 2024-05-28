from flask import Flask, render_template,request

app = Flask(__name__)

@app.post('/')
def user():
    # user = {}
    user  = request.form.get("last_name")
    # user[last_name] = request.form.get("last_name")
    # user[email] = request.form.get("email")
    # user[phone]= request.form.get("phone")
    # user[password] = request.form.get("password") 
    # user[usertype] = request.form.get("usertype")
    # return "<p><p>"
    return render_template('http://127.0.0.1:3000/index.html')

if __name__ == '__main__':
    app.run(debug=True)