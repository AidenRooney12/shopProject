from flask import Flask, render_template

from controllers.brandController import brands_blueprint
from controllers.shoeController import shoes_blueprint


app = Flask(__name__)

app.register_blueprint(brands_blueprint)
app.register_blueprint(shoes_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)