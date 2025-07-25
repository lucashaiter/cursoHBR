'''
# Ex1
from datetime import datetime, timedelta
print(f"Data e hora atual: {datetime.now().strftime("%d/%m/%y")}")
print(f"Data de ontem: {(datetime.now() - timedelta(days=1)).strftime("%d/%m/%y")}")
data1 = datetime(2023, 10, 1)
data2 = datetime(2023, 10, 31)
print(f"Diferença entre {data2.strftime("%d/%m/%y")} e {data1.strftime("%d/%m/%y")}: {(data2 - data1).days} dias")


# Ex2
import emoji

mensagem = emoji.emojize("smile")
print(mensagem)
'''

# Ex4
import requests

url = "https://api.github.com/users/lucashaiter"
resposta = requests.get(url)
dados = resposta.json()
print(f"Nome: {dados.get('name')}")
print(f"URL do perfil: {dados.get('html_url')}")

# Ex5
# 1 - Criar um ambiente virtual (python -m venv venv1)
# 2 - Entrar no venv1 (\venv1\Scripts\activate)
# 3 - Instalar um lib qualquer (pip install django)
# 4 - Verificar se foi instalado (pip list)
# 5 - Gerando o arquivo requirements.txt (pip freeze > requirements.txt)
# 6 - Sair do ambiente virtual (deactivate)
# 7 - Criar um novo ambiente virtual (python -m venv venv2)
# 8 - Entrar no venv2 (\venv3\Scripts\activate)
# 9 - Instalando dependencias a partir de um arquivo (pip install -r requirements.txt)
# 10 - Exercício finalizado!