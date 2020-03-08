from flask import Flask,render_template,abort
import datetime
app = Flask(__name__)

@app.route('/')
def home():

    return render_template('pages/home.html')
    
@app.route('/cv')
def cv():
    # retourne un template page html
    return render_template('pages/cv.html')

@app.route('/motivation')
def motivation():
    # retourne un template page html
    return render_template('pages/motivation.html')

@app.route('/service')
def service():
    # retourne un template page html
    return render_template('pages/service.html')



""" gestion d'erreur 404 """
@app.errorhandler(404)
def page_not_found(error):

    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run(debug = True,host = '0.0.0.0',port = '5000')
