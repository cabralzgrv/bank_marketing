# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import scipy

# Função para criar histograma com linha da mediana, média, moda e curva de densidade
def histogram(dataframe, feature_name, bins=30, figsize=(10, 6)):
    # Verificar se a feature existe no dataframe
    if feature_name not in dataframe.columns:
        print(f"Erro: A feature '{feature_name}' não existe no DataFrame.")
        return
    
    # Verificar se a feature é numérica
    if not pd.api.types.is_numeric_dtype(dataframe[feature_name]):
        print(f"Erro: A feature '{feature_name}' não é numérica.")
        return
    
    # Criar a figura e o eixo
    plt.figure(figsize=figsize)
    
    # Criar o histograma com densidade normalizada
    ax = dataframe[feature_name].hist(bins=bins, edgecolor='black', density=True, alpha=0.7)
    
    # Adicionar a curva de densidade (o "sino")
    sns.kdeplot(dataframe[feature_name], color='purple', lw=2, label='Curva de Densidade')
    
    # Calcular a mediana, moda e média
    mean_value = dataframe[feature_name].mean()
    mode_value = dataframe[feature_name].mode()[0]
    median_value = dataframe[feature_name].median()
    
    # Adicionar a linha da mediana, moda e média
    plt.axvline(x=mean_value, color='blue', linestyle='--', linewidth=1, alpha=0.5,label=f'Média: {mean_value:.2f}')
    plt.axvline(x=mode_value, color='green', linestyle='--', linewidth=1, alpha=0.5, label=f'Moda: {mode_value:.2f}')
    plt.axvline(x=median_value, color='red', linestyle='--', linewidth=1, alpha=0.5, label=f'Mediana: {median_value:.2f}')
    
    # Configurar o título e as legendas
    plt.title(f'Distribuição de {feature_name}', color='black', fontsize=14)
    plt.xlabel(feature_name, fontsize=12)
    plt.ylabel('Densidade', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Estatisticas descritivas
    print(f"Estatísticas descritivas para {feature_name}:")
    print(f"  - Máximo: {dataframe[feature_name].max()}")
    print(f"  - Mínimo: {dataframe[feature_name].min()}")
    print(f"  - Amplitude: {dataframe[feature_name].max() - dataframe[feature_name].min():.2f}")
    print(f"  - Média: {mean_value:.2f}")
    print(f"  - Mediana: {median_value:.2f}")
    print(f"  - Moda: {mode_value:.2f}")
    print(f"  - Variância: {dataframe[feature_name].var():.2f}")
    print(f"  - Desvio Padrão: {dataframe[feature_name].std():.2f}")
    print(f"  - IIQ: {dataframe[feature_name].quantile(0.75) - dataframe[feature_name].quantile(0.25):.2f}")

    
    # Calcular e mostrar estatísticas descritivas relacionadas à normalidade
    skewness = stats.skew(dataframe[feature_name])
    kurtosis = stats.kurtosis(dataframe[feature_name])
    
    print(f"\nEstatísticas adicionais relevantes para normalidade:")
    print(f"Assimetria (Skewness): {skewness:.4f}")
    print(f"  - Valores próximos de 0 indicam simetria (característica da normalidade)")
    print(f"  - Valores > 0 indicam assimetria positiva (cauda à direita)")
    print(f"  - Valores < 0 indicam assimetria negativa (cauda à esquerda)")
    
    print(f"Curtose (Kurtosis): {kurtosis:.4f}")
    print(f"  - Valores próximos de 0 indicam distribuição similar à normal")
    print(f"  - Valores > 0 indicam distribuição mais 'pontiaguda' que a normal")
    print(f"  - Valores < 0 indicam distribuição mais 'achatada' que a normal")
    
    pass