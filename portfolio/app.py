from flask import *
from portfolio.model.model import Model
import hashlib
import datetime
model =Model('data')
app = Flask(__name__)

#-----------------------------------------admin------------------------------------------
@app.route('/login')
def login():
    return render_template('admin/login.html')
email = 'email@email'
password = hashlib.sha1(b'bruno2020').digest()
@app.route('/admin')
def admin():
    if email == 'email@email' and password != b'lC[\xc5\xc6\xa0\x08\xf8:\x16\x95\x97\xac\xdd?|\xbek\x10`':
        return redirect(url_for('login'))
    elif email != 'email@email': 
        abort(401)
    return render_template('admin/admin.html')

#---------------------------------------- end admin--------------------------------------

#-----------------------------------------visitor--------------------------------------------
@app.route('/')
def home():
    return render_template('pages/home.html')

@app.route('/service')
def service():
    #model.add_service('application bureau','JAVA,PYTHON','tikinter, JFrame')
    #model.delete_service('application bureau')
    liste = model.display_all_service()
    return render_template('pages/service.html',liste = liste)

@app.context_processor
def inject_now():
    return dict(now=datetime.datetime.now().year)
#------------------------------------------end visitor-----------------------------------------

#---------------------------------------------------error---------------------------------------
""" gestion d'erreur 404 """
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

"""  gestion d'erreur 401 """
@app.errorhandler(401)
def non_autorise(error):
    return render_template('errors/401.html'), 401
#-----------------------------------------------end error---------------------------------------

#-----------------------------------------------run---------------------------------------------
if __name__ == '__main__':
    app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'
    app.run(debug = True,host = '0.0.0.0',port = '5000')
#--------------------------------------------end run--------------------------------------------

