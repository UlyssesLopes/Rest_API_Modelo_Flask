import json
from flask import Flask, jsonify, request

app = Flask(__name__)

pontos = [
    
]


@app.route('/ponto/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_put_delete_registros_com_id(id):
    if request.method == 'GET':
        try:
            response = pontos[id]
           
        except IndexError:
            mensagem = 'Registro de ID: {} nao encontrado.'.format(id)
            response = {'status': 'ERRO', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido, procure o adminstrador do sistema.'
            response = {'status': 'ERRO', 'mensagem': mensagem}

        return jsonify(response)  

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        pontos[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        pontos.pop(id)
        mensagem = 'Registro excluído com sucesso!'
        return jsonify({'status': 'SUCCESS', 'mensagem': mensagem})


@app.route('/ponto/', methods=['GET', 'POST'])
def get_post_registros_de_ponto():
    if request.method == 'POST':
        dados = json.loads(request.data)
        pontos.append(dados)

        mensagem = 'Registro inserido com sucesso!'
        return jsonify({'ststus': 'SUCCESS', 'mensagem': mensagem})
    
    elif request.method == 'GET':
        return jsonify(pontos)

if __name__=="__main__":
    app.run(debug=True)