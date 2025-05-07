# Sistema de Pesquisa de Satisfação

Sistema moderno de pesquisa de satisfação com interface de chat, desenvolvido em Python com Flask.

## Características

- Interface de chat moderna e responsiva
- Suporte a diferentes tipos de pesquisa (Vendas, Administrativo, Seguros)
- Sistema de mensagens orientado a middleware (MOM)
- Exportação de dados em CSV
- Design adaptativo para desktop e mobile
- Feedback visual para cada resposta

## Requisitos

- Python 3.8+
- Flask 3.0.2
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd pesquisa_satisfacao_app
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando o Projeto

1. Configure as variáveis de ambiente (opcional):
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

2. Execute o servidor:
```bash
python src/app.py
```

3. Acesse a aplicação em `http://localhost:5000`

## Estrutura do Projeto

```
pesquisa_satisfacao_app/
├── src/
│   ├── app.py              # Aplicação principal
│   ├── routes/             # Rotas da aplicação
│   ├── models/             # Modelos de dados
│   ├── mom/                # Sistema de mensagens
│   └── templates/          # Templates HTML
├── data/                   # Dados das pesquisas
├── exports/                # Arquivos exportados
├── requirements.txt        # Dependências
└── README.md              # Documentação
```

## Uso

1. Acesse a página inicial
2. Selecione o tipo de pesquisa desejado
3. Responda às perguntas através da interface de chat
4. Ao finalizar, os dados são salvos automaticamente
5. Use o botão de exportação para baixar os dados em CSV

## Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes. 