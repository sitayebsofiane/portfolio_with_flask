from flask import Flask,render_template,abort,request,redirect
import datetime
from Pillow import Image
from StringIO import StringIO

app = Flask(__name__)

#-----------------------------------------admin------------------------------------------
@app.route('/admin')
def login():
    return render_template('admin/login.html')
#---------------------------------------- end admin--------------------------------------
#------------------------------------test------------------------------------------------
@app.route('/test')
def test():
    return render_template('admin/test.html')

#----------------------------------------------------------------------------------------
#-----------------------------------------visitor--------------------------------------------
@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/service')
def service():
    # retourne un template page html
    return render_template('pages/service.html')

@app.context_processor
def inject_now():
    return dict(now=datetime.datetime.now().year)
#------------------------------------------end visitor-----------------------------------------
""" gestion d'erreur 404 """
@app.errorhandler(404)
def page_not_found(error):

    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run(debug = True,host = '0.0.0.0',port = '5000')

