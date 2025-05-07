from flask import Blueprint, render_template, request, jsonify, redirect, url_for, send_file
from src.models.survey import Survey
from src.mom.message_handler import MessageHandler
import json
from datetime import datetime
import csv
import io

survey_bp = Blueprint('survey', __name__)

@survey_bp.route('/survey/<survey_type>', methods=['GET', 'POST'])
def show_survey(survey_type):
    if survey_type not in ['vendas', 'administrativo', 'seguros']:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        try:
            data = request.get_json() if request.is_json else request.form
            
            # Salvar no banco de dados
            survey = Survey(
                survey_type=survey_type,
                responses=data,
                created_at=datetime.now()
            )
            survey.save()
            
            # Criar e salvar mensagem
            message = MessageHandler()
            message.create_survey_message(survey_type=survey_type, responses=data)
            message.save_to_json()
            
            if request.is_json:
                return jsonify({'success': True})
            return redirect(url_for('index'))
            
        except Exception as e:
            print(f"Erro ao processar pesquisa: {str(e)}")
            if request.is_json:
                return jsonify({'success': False, 'error': str(e)}), 400
            return redirect(url_for('index'))
    
    # Definir perguntas baseadas no tipo de pesquisa
    questions = []
    feedback_labels = []
    
    if survey_type == 'vendas':
        questions = [
            "Como você avalia o atendimento inicial?",
            "Como você avalia o conhecimento do produto pelo vendedor?",
            "Como você avalia a negociação e condições de pagamento?",
            "Como você avalia a entrega do veículo?",
            "Como você avalia a apresentação do veículo na entrega?"
        ]
        feedback_labels = [
            "Precisamos melhorar muito nosso atendimento",
            "Temos muito a melhorar",
            "Estamos no caminho certo",
            "Estamos quase lá",
            "Excelente! Continuaremos assim"
        ]
    elif survey_type == 'administrativo':
        questions = [
            "Como você avalia o atendimento da equipe administrativa?",
            "Como você avalia a clareza nas informações fornecidas?",
            "Como você avalia o tempo de resposta?",
            "Como você avalia a resolução do seu problema?",
            "Como você avalia a cordialidade no atendimento?"
        ]
        feedback_labels = [
            "Precisamos melhorar muito nosso atendimento",
            "Temos muito a melhorar",
            "Estamos no caminho certo",
            "Estamos quase lá",
            "Excelente! Continuaremos assim"
        ]
    elif survey_type == 'seguros':
        questions = [
            "Como você avalia o atendimento do corretor?",
            "Como você avalia a clareza na explicação das coberturas?",
            "Como você avalia o preço do seguro?",
            "Como você avalia a rapidez na contratação?",
            "Como você avalia a resolução de sinistros (se aplicável)?"
        ]
        feedback_labels = [
            "Precisamos melhorar muito nosso atendimento",
            "Temos muito a melhorar",
            "Estamos no caminho certo",
            "Estamos quase lá",
            "Excelente! Continuaremos assim"
        ]
    
    # Exibir lembrete para vendas e administrativo
    show_review_reminder = survey_type in ['vendas', 'administrativo']
    
    return render_template('chat_survey.html',
                         survey_type=survey_type,
                         questions=questions,
                         feedback_labels=feedback_labels,
                         show_review_reminder=show_review_reminder,
                         location=request.args.get('location', 'Unidade Central'))

@survey_bp.route('/export')
def export_surveys():
    try:
        surveys = Survey.get_all()
        
        if not surveys:
            return "Nenhuma pesquisa encontrada para exportar.", 404
        
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(['Tipo', 'Respostas', 'Data'])
        
        for survey in surveys:
            writer.writerow([
                survey.survey_type,
                json.dumps(survey.responses, ensure_ascii=False),
                survey.created_at.strftime('%d/%m/%Y %H:%M:%S')
            ])
        
        output.seek(0)
        return send_file(
            io.BytesIO(output.getvalue().encode('utf-8')),
            mimetype='text/csv',
            as_attachment=True,
            download_name=f'pesquisas_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        )
        
    except Exception as e:
        print(f"Erro ao exportar pesquisas: {str(e)}")
        return "Erro ao exportar pesquisas.", 500 