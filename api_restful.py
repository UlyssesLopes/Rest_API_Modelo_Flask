from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import os

# ==================== API CONTROLE REGISTROS DE PONTO ==============================

app = Flask(__name__)
CORS(app)
api = Api(app)

# ==================== LISTA DE VALORES ======================
pontos = []

"""  MODELO DE DADOS JSON

    {   
        'id': '0',
        'colaborador': 'Default',
        'localizacao': 'Default',
        'data_batida': 'Default',
        'hora_batida': 'Default',
        'acao_ponto': 'Default'
    }

"""


# =================== CLASSE DE REGISTROS COM OS MÉTODOS GET, PUT E DELETE ======================
class Registros(Resource):
    def get(self, id):
        try:
            response = pontos[id]

        except IndexError:
            mensagem = 'Registro de ID: {} nao encontrado.'.format(id)
            response = {'status': 'ERRO', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido, procure o adminstrador do sistema.'
            response = {'status': 'ERRO', 'mensagem': mensagem}

        return response

    def put(self, id):
        try:
            response = json.loads(request.data)
            pontos[id] = response

        except Exception:
            mensagem = 'Nao foi possível atualizar o registro desejado.'
            response = {'status': 'ERRO', 'mensagem': mensagem}

        return response

    def delete(self, id):
        try:
            pontos.pop(id)
            mensagem = 'Registro excluído com sucesso!'
            response = {'status': 'SUCCESS', 'mensagem': mensagem}
        
        except Exception:
            mensagem = 'Erro desconhecido, nao foi possível deletar o registro.'
            response = {'status': 'ERRO', 'mensagem': mensagem}

        return response


# =================== CLASSE PARA LISTA DE TODOS OS REGISTROS COM OS MÉTODOS GET E POST ======================
class TodosRegistros(Resource):
    def get(self):
        return pontos

    def post(self):
        try:
            response = json.loads(request.data)
            pontos.append(response)

            posicao = len(pontos)
            response['id'] = posicao

            mensagem = 'Registro inserido com sucesso!'
            response = {'status': 'SUCCESS', 'mensagem': mensagem}
        
        except Exception:
            mensagem = 'Nao foi possível inserir o registro!'
            response = {'status': 'ERROR', 'mensagem': mensagem}
        
        return response


# ================= CHAMADAS DE URL ===========================
api.add_resource(Registros, '/ponto/<int:id>')
api.add_resource(TodosRegistros, '/registros/')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
