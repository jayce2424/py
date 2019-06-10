#encoding:utf-8

from flask import Flask, render_template


app = Flask(__name__)

#for遍历字典
@app.route('/')
def index():
    # user = {
    #     'username': 'jqx',
    #     'age': 18
    # }
    # websites= ['baidu.com','google.com']

    # return render_template('index.html', user=user,websites=websites)
    books = [
        {
            'name':u'西游记',
            'author':u'wce',
            'price':109

        },
        {
            'name': u'西游记2',
            'author': u'wce2',
            'price': 1099
        },
        {
            'name': u'西游记3',
            'author': u'wce3',
            'price': 10998
        }

    ]
    return render_template('index.html', books=books)

if __name__=='__main__':
    app.run(debug=True)