# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#    return 'Hello World'

# if __name__ == '__main__':
#    app.run()
# from flask import Flask

# 쿼리스트링 처럼 값을 줄 수 있음
# app = Flask(__name__)

# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name

# if __name__ == '__main__':
#    app.run(debug=True)

# from flask import Flask
# app = Flask(__name__)

# @app.route('/flask') # url 정의
# def hello_flask():
#    return 'Hello Flask'

# @app.route('/python/')
# def hell0_python():
#    return 'Hello Python'

# if __name__ == '__main__':
#    app.run()

# url_for()로 들어오는 값에 따라 페이지를 다르게 띄울수 있음
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))
   
if __name__ == '__main__':
   app.run(debug = True)