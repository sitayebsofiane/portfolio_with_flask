from flask import Flask,render_template,abort
from flask_sqlalchemy import SQLAlchemy
import datetime
app = Flask(__name__)
#--------------------------------------------------------conect to bdd---------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:as122014@localhost:5432/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'bruno'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'username:{self.username} eamil{self.email} #####'

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

#---------------------------------------------------------blog----------------------------------------------------------
from post import Post

@app.route('/blog/')
def blog():
    # u =User(username ='emira',email ='emira')
    # db.session.delete(u)
    # db.session.commit()
    tout = User.query.first()
    return render_template('posts/index.html',bruno = Post.all(),tout = tout)
      
#<id> c'est un parametre qui va etre reçu par la fonction
@app.route('/blog/posts/<int:id>')
def posts_show(id):
    try: 
        return render_template('posts/show.html',bruno = Post.find(id))
    except:
        abort(404)

@app.context_processor
def inject_now():
   
    return dict({'now': datetime.datetime.now().year})


@app.context_processor
def utility_processor():
    def pluralize(count,singular,plural=None):
        if not isinstance(count,int):
            raise ValueError(f'{count} must be an integer')
        if plural is None :
            plural = singular +'s'
        if count == 1:
            res = singular
        else:
            res = plural
        return f'{count} {res}'
    return dict(nom_dans_vue = pluralize)

""" gestion d'erreur 404 """
@app.errorhandler(404)
def page_not_found(error):

    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True,host = '0.0.0.0',port = '5000')
