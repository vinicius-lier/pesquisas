from typing import Dict, Any
import json
from datetime import datetime
import os

class MessageHandler:
    def __init__(self):
        self.message_queue = []

    def create_survey_message(self, survey_type: str, responses: Dict[str, Any]) -> Dict[str, Any]:
        """
        Cria uma mensagem MOM para uma resposta de pesquisa
        """
        message = {
            "type": "SURVEY_RESPONSE",
            "timestamp": datetime.now().isoformat(),
            "payload": {
                "survey_type": survey_type,
                "responses": responses
            }
        }
        self.message_queue.append(message)
        return message

    def create_export_message(self) -> Dict[str, Any]:
        """
        Cria uma mensagem MOM para exportação de dados
        """
        message = {
            "type": "EXPORT_REQUEST",
            "timestamp": datetime.now().isoformat(),
            "payload": {
                "format": "CSV"
            }
        }
        self.message_queue.append(message)
        return message

    def get_messages(self) -> list:
        """
        Retorna todas as mensagens na fila
        """
        return self.message_queue

    def clear_messages(self):
        """
        Limpa a fila de mensagens
        """
        self.message_queue = []

    def save_to_json(self):
        """
        Salva as mensagens em um arquivo JSON
        """
        data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        os.makedirs(data_dir, exist_ok=True)
        
        filepath = os.path.join(data_dir, 'messages.json')
        
        # Carregar mensagens existentes
        messages = []
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                messages = json.load(f)
        
        # Adicionar novas mensagens
        messages.extend(self.message_queue)
        
        # Salvar todas as mensagens
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)

    def load_messages_from_file(self, filename: str):
        """
        Carrega mensagens de um arquivo JSON
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.message_queue = json.load(f)
        except FileNotFoundError:
            self.message_queue = [] 