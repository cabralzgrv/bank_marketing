# Análise Exploratória de Dados de Marketing Bancário

## Sobre o Projeto

Este projeto realiza uma análise exploratória detalhada de um conjunto de dados de campanhas de marketing de uma instituição bancária portuguesa. O conjunto de dados contém informações sobre ligações telefônicas e tem como objetivo principal entender quais fatores influenciam a decisão dos clientes em adquirir um depósito a prazo bancário.

## Fonte de Dados

Os dados foram obtidos do UCI Machine Learning Repository: [Bank Marketing Dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing)

## Estrutura do Projeto

```
bank-marketing-analysis/
│
├── data/
│   └── bankadditionalfull.csv
│
├── notebooks/
│   ├── 1_exploratory_data_analysis.ipynb
│   └── 2_feature_relationships.ipynb
│
├── src/
│   ├── __init__.py
│   ├── visualization.py
│   ├── statistics.py
│   └── utils.py
│
├── README.md
└── requirements.txt
```

## Configuração do Ambiente

```bash
# Clonar o repositório
git clone https://github.com/cabralzgrv/bank-marketing-analysis.git
cd bank-marketing-analysis

# Criar e ativar ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

## Análise Exploratória Passo a Passo

### 1. Compreensão e Preparação dos Dados

- Importação do dataset
- Verificação da estrutura dos dados (separados por ponto-e-vírgula)
- Análise inicial das variáveis disponíveis
- Tratamento de valores ausentes e atípicos

### 2. Análise Univariada

#### 2.1 Distribuição de Idade dos Clientes
- Criação de histograma com estatísticas (média, mediana, moda)
- Análise de boxplot para identificação de outliers
- Testes de normalidade nas variáveis numéricas

#### 2.2 Distribuição de Profissões
- Contagem e visualização das profissões mais comuns
- Análise percentual das principais ocupações dos clientes

#### 2.3 Formas de Contato
- Análise da distribuição das diferentes formas de contato
- Comparação percentual entre os métodos utilizados

### 3. Análise Bivariada

#### 3.1 Relação entre Idade e Saldo Bancário
- Gráficos de dispersão para visualizar correlações
- Análise de correlação de Pearson
- Identificação de padrões entre as variáveis

#### 3.2 Identificação e Análise de Outliers
- Aplicação do método interquartil para identificação de outliers
- Comparação entre clientes outliers e não-outliers:
  - Taxas de adesão ao produto bancário
  - Distribuição de idades
  - Distribuição de saldos
  - Distribuição temporal (ocorrência por mês)

#### 3.3 Variáveis Determinantes para Adesão
- Análise da influência de inadimplência na adesão
- Comparação entre clientes com e sem empréstimos/financiamentos
- Identificação das variáveis mais determinantes para aquisição do produto

### 4. Análise Multivariada

#### 4.1 Correlações entre Variáveis Numéricas
- Cálculo e visualização de matriz de correlação
- Criação de mapa de calor para facilitar a interpretação

#### 4.2 Relações entre Variáveis Categóricas
- Exploração de conversão de depósitos considerando múltiplas variáveis
- Análise de mapas de calor para variáveis categóricas combinadas
- Identificação de padrões de adesão baseados em combinações de características

### 5. Probabilidade Condicional

- Cálculo da probabilidade de adesão dado contato prévio
- Análise de como contatos anteriores influenciam a decisão

### 6. Modelagem (Bônus)

- Desenvolvimento de modelo de classificação usando as features analisadas
- Aplicação de permutation importance para identificar variáveis mais impactantes

## Principais Ferramentas Utilizadas

- **Python**: Linguagem de programação principal
- **Pandas**: Manipulação e análise dos dados
- **NumPy**: Operações numéricas
- **Matplotlib/Seaborn**: Visualização de dados
- **SciPy**: Testes estatísticos de normalidade e correlação
- **Scikit-learn** : Para modelagem e machine learning

## Testes de Normalidade

Implementei testes abrangentes de normalidade para entender a distribuição das variáveis numéricas:

- **Shapiro-Wilk**: Ideal para amostras menores
- **Kolmogorov-Smirnov**: Para amostras maiores
- **D'Agostino-Pearson**: Combinando testes de assimetria e curtose
- **Anderson-Darling**: Análise com ênfase nas caudas da distribuição

Os resultados destes testes foram fundamentais para determinar quais métodos estatísticos seriam mais apropriados nas análises subsequentes.

## Insights Principais

- A distribuição de idade dos clientes apresenta assimetria positiva, com concentração maior em adultos jovens
- Existem correlações significativas entre determinadas variáveis econômicas e a propensão à adesão
- O nível educacional do cliente apresenta forte relação com a taxa de conversão
- Contatos prévios aumentam significativamente a probabilidade de adesão ao produto bancário

## Conclusões e Recomendações

Com base nas análises realizadas, identificamos os principais fatores que influenciam a adesão ao depósito a prazo e desenvolvemos recomendações para otimização das campanhas de marketing do banco.

## Próximos Passos

- Aprofundamento da análise de segmentos específicos identificados
- Desenvolvimento de modelos preditivos mais sofisticados
- Criação de uma estratégia de marketing personalizada baseada nos insights obtidos

---

## Autor

Lucas Cabral Araújo
EMAIL - lucascabralaraujo@outlook.com
LINKEDIN - https://www.linkedin.com/in/lucascabralaraujo/
