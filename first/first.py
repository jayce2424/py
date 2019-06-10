#encoding:utf-8

from flask import Flask, redirect, url_for, render_template
import config
#反转带有视图参数的函数
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    # print url_for('my_list')
    #print url_for('article',id='abc')
    #页面跳转和重定向
    #法1：return redirect('/login/')
    #法2推荐：
    #login_url = url_for('login')
    #return redirect(login_url)
    #return u'这是首页'
    #return render_template('index.html', username=u'季千翔')
    #多个参数渲染
    class Person(object):
        name = u'分辨率'
        age = 19

    p = Person()

    context = {
        'username': u'季千翔',
        'gender': u'男',
        'age': 18,
        'person': p,
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('index.html', **context)

@app.route('/list/')
def my_list():
    return 'list'

@app.route('/login/')
def login():
    return '这是登录页面'

@app.route('/article/<id>')
def article(id):
    return u'您请求的参数是：%s' % id

@app.route('/question/<is_login>')
def question(is_login):
    if is_login=='1':
        return '这是发布问答页面'
    else:
        return redirect(url_for('login'))

if __name__=='__main__':
    app.run()