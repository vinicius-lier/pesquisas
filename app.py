from flask import Flask, render_template
from src.models.survey_models import db
from src.routes.survey_routes import survey_bp
import os

app = Flask(__name__, template_folder='src/templates', static_folder='src/static')

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this in a real application

db.init_app(app)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

# Register Blueprints here
app.register_blueprint(survey_bp, url_prefix='/surveys')

@app.route('/')
def home():
    # Simple home page linking to the surveys
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True) 