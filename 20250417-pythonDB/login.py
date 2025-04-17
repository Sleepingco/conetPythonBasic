from flask import Flask, redirect,url_for,request,render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name
@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form['nm']
        return redirect(url_for('success',name = user)) # 쿼리스트링으로 받아서 po
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))


if __name__ == '__main__':
    app.run(debug=True)

# 127.0.0.1 - - [17/Apr/2025 16:29:20] "POST /login HTTP/1.1" 302 -
# 127.0.0.1 - - [17/Apr/2025 16:29:20] "GET /success/aaa HTTP/1.1" 200 -