from datetime import datetime
import json
import os

class Survey:
    def __init__(self, survey_type, responses, created_at=None):
        self.survey_type = survey_type
        self.responses = responses
        self.created_at = created_at or datetime.now()
    
    def save(self):
        """Salva a pesquisa no arquivo JSON"""
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        filepath = os.path.join(data_dir, 'surveys.json')
        
        # Carregar pesquisas existentes
        surveys = []
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                surveys = json.load(f)
        
        # Adicionar nova pesquisa
        survey_data = {
            'survey_type': self.survey_type,
            'responses': self.responses,
            'created_at': self.created_at.isoformat()
        }
        surveys.append(survey_data)
        
        # Salvar todas as pesquisas
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(surveys, f, ensure_ascii=False, indent=2)
    
    @classmethod
    def get_all(cls):
        """Retorna todas as pesquisas salvas"""
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        filepath = os.path.join(data_dir, 'surveys.json')
        
        if not os.path.exists(filepath):
            return []
        
        with open(filepath, 'r', encoding='utf-8') as f:
            surveys_data = json.load(f)
        
        return [
            cls(
                survey_type=data['survey_type'],
                responses=data['responses'],
                created_at=datetime.fromisoformat(data['created_at'])
            )
            for data in surveys_data
        ]
    
    @classmethod
    def get_by_type(cls, survey_type):
        """Retorna todas as pesquisas de um tipo específico"""
        return [s for s in cls.get_all() if s.survey_type == survey_type] 