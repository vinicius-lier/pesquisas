from flask import Flask, render_template
from routes.survey_routes import survey_bp

app = Flask(__name__)

# Registrar o blueprint
app.register_blueprint(survey_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True) 