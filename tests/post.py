import requests

BASE = 'http://127.0.0.1:5000/registros/'

pontos = {'id': '', 'colaborador': 'Ulysses Lopes', 'localizacao': 'Rua Riachuelo 934', 'data_batida': '18/10/2022', 'hora_batida': '11:30', 'acao_ponto': '1 Saída'}

response = requests.post(BASE, json = pontos)
print(response.json())

