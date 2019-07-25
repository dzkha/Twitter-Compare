from flask import Flask, request, render_template
from .models import DB, User

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config('SQLALCHEMY_DATABASE_URI') = 'sqlite:///db.sqlite3'
    app.config['ENV'] = 'debug' 
    DB.init_app(app)
    
    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    
    @app.route("/predictions")
    def preds():
        return render_template('home.html')

    @app.route('/iris')
    def iris():    
        from sklearn.datasets import load_iris
        from sklearn.linear_model import LogisticRegression
        X, y = load_iris(return_X_y=True)
        clf = LogisticRegression(random_state=0, solver='lbfgs',
                          multi_class='multinomial').fit(X, y)
        return str(clf.predict(X[:2, :]))
    
    return app


#if __name__ == "__main__":
#    app.run(debug=True)
