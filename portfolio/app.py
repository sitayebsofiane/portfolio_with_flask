from flask import *
import datetime
from PIL import Image

app = Flask(__name__)

#-----------------------------------------admin------------------------------------------
@app.route('/login')
def login():
    return render_template('admin/login.html')
email = 'hhhh'
password='123'
@app.route('/admin')
def admin():
    if email == 'email@email' and password != '123':
        return redirect(url_for('login'))
    elif email != 'email@email': 
        abort(401)
    return render_template('admin/admin.html')

#---------------------------------------- end admin--------------------------------------
#------------------------------------test------------------------------------------------
@app.route('/test')
def test():
    mots = ["bonjour", "à", "toi,", "visiteur."]
    return render_template('admin/test.html', titre="Bienvenue !", mots=mots ,menu=email)


#----------------------------------------------------------------------------------------
#-----------------------------------------visitor--------------------------------------------
@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/service')
def service():
    return render_template('pages/service.html')

@app.context_processor
def inject_now():
    return dict(now=datetime.datetime.now().year)
#------------------------------------------end visitor-----------------------------------------
""" gestion d'erreur 404 """
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

"""  gestion d'erreur 401 """
@app.errorhandler(401)
def non_autorise(error):
    return render_template('errors/401.html'), 401

if __name__ == '__main__':
    app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'
    app.run(debug = True,host = '0.0.0.0',port = '5000')

