# Construindo API Para Deploy do Modelo de Deep Learning
# API

# Imports
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import joblib
import traceback
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
import warnings
warnings.filterwarnings('ignore')

# Carrega o modelo e o scaler com tratamento de erros
try:
    modelo_ba_final = tf.keras.models.load_model('modelo_ba.keras')
    scaler_ba_final = joblib.load('scaler_ba.joblib')
except Exception as e:
    print("Erro ao carregar o modelo ou o scaler:", e)
    traceback.print_exc()
    modelo_ba_final = None
    scaler_ba_final = None

# Cria a app
app = Flask(__name__)

# Cria a rota de previsão
@app.route('/predict', methods=['POST'])
def predict():

    # Tenta executar o bloco de código
    try:

        # Obtém os dados do request como JSON
        dados = request.get_json(force=True)

        # Verifica se os dados foram fornecidos
        if not dados:
            return jsonify({"error": "Nenhum dado fornecido"}), 400

        # Verifica se o modelo e o scaler estão carregados corretamente
        if not modelo_ba_final or not scaler_ba_final:
            return jsonify({"error": "Modelo ou scaler não carregados corretamente"}), 500

        # Prepara os dados de entrada no formato de array NumPy
        dados_ba = np.array([list(d.values()) for d in dados])

        # Padroniza os dados de entrada
        dados_ba_scaled = scaler_ba_final.transform(dados_ba)

        # Realiza a previsão usando o modelo
        previsao = modelo_ba_final.predict(dados_ba_scaled)

        # Converte a previsão para o formato de lista
        previsao_formato_lista = previsao.flatten().tolist()

        # Retorna a previsão como JSON
        return jsonify(previsao_umidade_solo = previsao_formato_lista)

    # Captura qualquer exceção durante a previção
    except Exception as e:
        
        # Imprime o erro no console
        print("Erro durante a predição:", e)
        
        # Imprime o traceback no console
        traceback.print_exc()
        
        # Retorna um erro como JSON
        return jsonify({"error": "Erro durante a predição", "message": str(e)}), 500

# Bloco principal e execução da app
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print("Erro ao iniciar o servidor:", e)
        traceback.print_exc()

