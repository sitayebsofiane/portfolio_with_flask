from flask import Flask,render_template

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
posts = list()
@app.route('/blog')
def blog():
    global posts
    posts =[
        {'id':1,'title':'frist post','content':'this my frist post'},
        {'id':2,'title':'second post','content':'this my second post'},
        {'id':3,'title':'third post','content':'this my third post'},
    ]
    return render_template('posts/index.html',bruno = posts)

#<id> c'est un parametre qui va etre reçu par la fonction
@app.route('/blog/posts/<int:id>')
def posts_show(id):
    
    post = posts[id-1]
    return render_template('posts/show.html',bruno = post)



""" gestion d'erreur 404 """
@app.errorhandler(404)
def page_not_found(error):

    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    app.run(debug = True,host = '0.0.0.0',port = '5000')
