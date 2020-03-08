from flask import Flask,render_template,abort
import datetime
app = Flask(__name__)


@app.route('/admin/<password>')
def admin(password):
    if password == 1:
        return render_template('admin/admin.html')
    else:
        return render_template('admin/non_autorise.html')

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

""" gestion d'erreur 404 """
@app.errorhandler(404)
def page_not_found(error):

    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run(debug = True,host = '0.0.0.0',port = '5000')
