# 🌱 Otimização de Irrigação com Deep Learning

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.20.0-orange.svg)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-API-red.svg)](https://keras.io/)

Modelo de Deep Learning para prever níveis de umidade do solo e otimizar sistemas de irrigação agrícola. O projeto usa redes neurais artificiais para ajudar produtores a economizar água e energia enquanto maximizam a produtividade das colheitas.

---

## 🎯 Problema de Negócio

Produtores rurais enfrentam um dilema diário:
- ❌ **Irrigar demais** = Desperdício de água, energia e dinheiro
- ❌ **Irrigar de menos** = Perda de produtividade e prejuízo

**Solução:** Um modelo de IA que prevê o nível ideal de umidade baseado em condições climáticas, características do solo e histórico de irrigação.

---

## 💡 Impacto Esperado

✅ **Redução de custos** com água e energia  
✅ **Aumento de produtividade** das colheitas  
✅ **Sustentabilidade** através do uso consciente de recursos  
✅ **Tomada de decisão baseada em dados**  

---

## 🎬 Demonstração

<details>
<summary>📊 <b>Ver resultados do modelo</b></summary>

### Métricas de Desempenho

| Métrica | Valor | Interpretação |
|---------|-------|---------------|
| **MAE (Teste)** | 12.01 | Erro médio de X pontos percentuais |
| **MSE (Teste)** | 192.46 | Erro quadrático médio |
| **Épocas Treinadas** | 44/100 | Early stopping ativado |

### Exemplo de Previsão

**Entrada:**
- Temperatura: 28°C
- Precipitação: 15mm
- Tipo de solo: Argiloso
- Dias desde última irrigação: 3

**Saída:**
- Umidade prevista: 65%
- Recomendação: Irrigar em 2 dias

</details>

---

### Componentes-Chave

**1. Camadas Densas (Fully Connected)**
- Progressão decrescente: 64 → 32 → 16 → 1
- Aprende padrões cada vez mais específicos

**2. Função de Ativação ReLU**
- Liga neurônios quando detectam padrões importantes
- Rápida e eficiente para treinar

**3. Dropout (30%)**
- Desliga aleatoriamente 30% dos neurônios
- Previne overfitting (decorar ao invés de aprender)

**4. Callbacks Inteligentes**
- **Early Stopping:** Para quando não há melhora por 10 épocas
- **Model Checkpoint:** Salva automaticamente a melhor versão

</details>

---

## 🛠️ Tecnologias Utilizadas

```python
Deep Learning & ML
├── TensorFlow 2.20.0        # Framework de Deep Learning
├── Keras API             # Interface simplificada
├── Scikit-learn          # Pré-processamento
└── NumPy/Pandas          # Manipulação de dados

Deploy
├── Joblib                # Serialização de objetos
└── StandardScaler        # Padronização (salvo para deploy)
```

---

## 📊 Dataset

**Características:**
- Features climáticas (temperatura, precipitação, etc.)
- Propriedades do solo
- Histórico de irrigação
- Target: Nível de umidade do solo (%)

**Divisão dos Dados:**
- 80% Treino (com 20% para validação interna)
- 20% Teste (nunca visto pelo modelo)

---

## 🚀 Como Executar

<details>
<summary><b>📥 Instruções completas</b></summary>

### Pré-requisitos
- Python 3.8+
- TensorFlow 2.20.0
- Jupyter Notebook

### Instalação

```bash
# Clone o repositório
git clone https://github.com/biasandrade/otimizacao-irrigacao-deep-learning.git

# Entre na pasta
cd otimizacao-irrigacao-deep-learning

# Instale as dependências
pip install -r requirements.txt

# Abra o notebook
jupyter notebook otimizacao-irrigacao-deep-learnin.ipynb
```

### Executando

O notebook está organizado em 11 etapas sequenciais:

1. **Instalação e Imports** - Preparar ambiente
2. **Carregamento de Dados** - Ler o dataset
3. **Análise Exploratória** - Entender os dados
4. **Limpeza** - Remover inconsistências
5. **Preparação** - Separar features e target
6. **Padronização** - Normalizar os dados
7. **Construção da Rede** - Definir arquitetura
8. **Compilação** - Configurar otimizador e métricas
9. **Callbacks** - Early Stopping + Checkpoint
10. **Treinamento** - Treinar o modelo
11. **Avaliação** - Testar e analisar resultados

Execute célula por célula e acompanhe o processo!

</details>

---

## 🧠 Conceitos Aplicados

### Machine Learning
- Supervised Learning (Regressão)
- Train/Test Split
- Feature Engineering
- Padronização (StandardScaler)

### Deep Learning
- Redes Neurais Artificiais (ANN)
- Forward Propagation
- Backpropagation
- Função de Perda (MSE)
- Otimização (Adam)
- Regularização (Dropout)
- Early Stopping

### Boas Práticas
- Validação cruzada
- Salvamento de modelos para deploy
- Callbacks inteligentes
- Código documentado e explicativo

---

## 💾 Arquivos Gerados

Após o treinamento, o projeto gera:

```
modelo_ba.keras          # Modelo treinado (deploy-ready)
scaler_ba.joblib         # Padronizador (para novos dados)
```

**Para fazer previsões:**
```python
import joblib
import tensorflow as tf

# Carregar modelo e scaler
modelo = tf.keras.models.load_model('modelo_ba.keras')
scaler = joblib.load('scaler_ba.joblib')

# Fazer previsão
novos_dados = [[28, 15, 3, ...]]  # Seus dados
dados_padronizados = scaler.transform(novos_dados)
previsao = modelo.predict(dados_padronizados)
print(f"Umidade prevista: {previsao[0][0]:.2f}%")
```

---

## 🔮 Próximos Passos

- [ ] API REST com Flask/FastAPI/Streamlit para deploy em produção
- [ ] Interface web para agricultores
- [ ] Integração com sensores IoT em tempo real
- [ ] Modelo de séries temporais (LSTM) para previsões futuras
- [ ] Dashboard de monitoramento com alertas
- [ ] Expandir para outras culturas agrícolas
- [ ] Otimização de hiperparâmetros (Grid Search)

---

## 📚 Aprendizados

Este projeto foi desenvolvido no curso da **Data Science Academy**.

**Competências desenvolvidas:**
✅ Deep Learning com TensorFlow/Keras  
✅ Arquitetura de redes neurais  
✅ Regularização e prevenção de overfitting  
✅ Callbacks e automação de treinamento  
✅ Preparação de modelos para deploy  
✅ Aplicação de IA em problemas reais do agronegócio  

---

## 👩‍💻 Autora

**Beatriz Andrade**  
18 anos com dados | 2024: Machine Learning

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Beatriz%20Andrade-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/andrade-beatriz/)
[![GitHub](https://img.shields.io/badge/GitHub-biasandrade-black?style=flat&logo=github)](https://github.com/biasandrade)
[![Email](https://img.shields.io/badge/Email-biasandrade%40gmail.com-red?style=flat&logo=gmail)](mailto:biasandrade@gmail.com)

---

## 📄 Licença

MIT License - use, modifique e aprenda à vontade!

---

⭐ Se este projeto te ajudou a entender Deep Learning aplicado, considera dar uma estrela!
