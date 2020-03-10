from flask import *
from portfolio.model.model import Model
import hashlib
import datetime
model =Model('data')
appli = Flask(__name__)

@appli.context_processor
def inject_now():
    return dict(now=datetime.datetime.now().year)
#-----------------------------------------admin------------------------------------------
@appli.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pseudo = request.form['pseudo']
        password = hashlib.sha1(request.form['password'].encode()).hexdigest()
        if request.form['pseudo'] == 'bruno' and password =='6c435bc5c6a008f83a169597acdd3f7cbe6b1060':
            return render_template('admin/admin.html')
        else:
            return redirect(url_for('login'))
    return render_template('admin/login.html')

@appli.route('/admin',methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        model.add_service(request.form.get('name_add'),request.form.get('techno'),request.form.get('outils'))
        model.delete_service(request.form.get('name_delete'))
        return render_template('admin/admin.html')
    else:
        return redirect(url_for('login'))

#---------------------------------------- end admin--------------------------------------

#-----------------------------------------visitor--------------------------------------------
@appli.route('/')
def home():
    return render_template('pages/home.html')

@appli.route('/service')
def service():
    #model.add_service('application bureau','JAVA,PYTHON','tikinter, JFrame')
    #model.delete_service('application bureau')
    liste = model.display_all_service()
    return render_template('pages/service.html',liste = liste)
#------------------------------------------end visitor-----------------------------------------

#---------------------------------------------------error---------------------------------------
""" gestion d'erreur 404 """
@appli.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404
#-----------------------------------------------end error---------------------------------------

#-----------------------------------------------run---------------------------------------------
if __name__ == '__main__':
    appli.run(debug = True)
#--------------------------------------------end run--------------------------------------------

