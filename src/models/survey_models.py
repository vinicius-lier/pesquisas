from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class SurveyResponse(db.Model):
    __tablename__ = 'survey_responses'

    id = db.Column(db.Integer, primary_key=True)
    survey_type = db.Column(db.String(50), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)
    q1_rating = db.Column(db.Integer, nullable=False)
    q2_rating = db.Column(db.Integer, nullable=False)
    q3_rating = db.Column(db.Integer, nullable=False)
    q4_rating = db.Column(db.Integer, nullable=False)
    open_feedback = db.Column(db.Text, nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<SurveyResponse {self.id} - {self.survey_type}>' 