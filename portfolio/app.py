from flask import Flask,render_template,abort

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

#---------------------------------------------------------blog----------------------------------------------------------
from post import Post

@app.route('/blog')
def blog():
    return render_template('posts/index.html',bruno = Post.all())
      
#<id> c'est un parametre qui va etre reçu par la fonction
@app.route('/blog/posts/<int:id>')
def posts_show(id):
    try:
        post = Post.find(id)
        return render_template('posts/show.html',bruno = post)
    except:
        abort(404)



""" gestion d'erreur 404 """
@app.errorhandler(404)
def page_not_found(error):

    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run(debug = True,host = '0.0.0.0',port = '5000')
