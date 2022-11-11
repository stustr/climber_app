from flask import Flask, render_template

from contollers.ascents_controller import ascents_blueprint
from contollers.climbers_controller import climbers_blueprint
from contollers.hills_controller import hills_blueprint

app = Flask(__name__)

app.register_blueprint(ascents_blueprint)
app.register_blueprint(climbers_blueprint)
app.register_blueprint(hills_blueprint)

@app.route("/")
def main():
    return render_template('index.html', title="Home")

if __name__ == '__main__':
    app.run()