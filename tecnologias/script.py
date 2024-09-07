"""
1. Python
Descrição: Python é uma linguagem de programação de alto nível, amplamente utilizada em ciência de dados, análise de dados e desenvolvimento web devido à sua simplicidade e versatilidade.

Instalação:

Baixe e instale o Python em python.org.
Verifique a instalação usando o comando no terminal: 
"""

python --version

""""
Recursos Úteis:
Documentação oficial: Python Documentation.
Ambiente recomendado: Jupyter Notebook, PyCharm ou VSCode.
"""

""" 
Biblioteca Pandas
Descrição: Pandas é uma biblioteca poderosa para análise e manipulação de dados, facilitando o trabalho com grandes volumes de dados e diferentes formatos, como CSV, JSON, e Excel.

Instalação:
No terminal, execute:
pip install pandas
"""

import pandas as pd

# Ler dados de um arquivo CSV
df = pd.read_csv('dados.csv')

# Exibir as 5 primeiras linhas do dataset
print(df.head())

""" 
Recursos Úteis:

Guia de Referência: Pandas Documentation.

"""

""" 
3. Biblioteca NumPy
Descrição: NumPy é uma biblioteca essencial para
operações matemáticas e manipulação de arrays multidimensionais em Python.
pip install numpy
"""

import numpy as np

# Criar um array
array = np.array([1, 2, 3, 4, 5])

# Calcular a média dos valores
media = np.mean(array)
print(media)

""" 
Recursos Úteis:

Guia de Referência: NumPy Documentation.
"""

""""
Biblioteca Matplotlib
Descrição: Matplotlib é uma biblioteca usada para criar gráficos e 
visualizações de dados, essencial para análises visuais em projetos de Big Data.

Instalação:
No terminal, execute:

pip install matplotlib
"""
import matplotlib.pyplot as plt

# Criar um gráfico simples
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title('Exemplo de Gráfico')
plt.show()

"""
Recursos Úteis:

Guia de Referência: Matplotlib Documentation.
"""

""" 
Biblioteca Seaborn
Descrição: Seaborn é uma biblioteca para visualização de dados que fornece interfaces de alto nível para criar gráficos
estatísticos atrativos e informativos.

Instalação:
No terminal, execute:
pip install seaborn
"""

import seaborn as sns
import matplotlib.pyplot as plt

# Usar um dataset embutido no Seaborn
df = sns.load_dataset('tips')

# Criar um gráfico de dispersão
sns.scatterplot(data=df, x='total_bill', y='tip')
plt.show()

""" 
Recursos Úteis:

Guia de Referência: Seaborn Documentation. 
"""

""" 
Jupyter Notebook
Descrição: Jupyter Notebook é uma ferramenta que permite criar e compartilhar documentos que contêm código,
visualizações e texto explicativo.

Instalação:
No terminal, execute:
pip install notebook

Iniciar o Jupyter Notebook:


jupyter notebook

Recursos Úteis:

Guia de Referência: Jupyter Documentation.
"""

"""
Git para Controle de Versão
Descrição: Git é um sistema de controle de versão amplamente utilizado para 
gerenciar projetos de software. GitHub é uma plataforma de hospedagem para 
repositórios Git.

Instalação:
No terminal, execute:

sudo apt install git  # Linux
brew install git      # macOS
Comandos Básicos:


# Inicializar um repositório
git init

# Adicionar arquivos ao controle de versão
git add .

# Commitar alterações
git commit -m "Descrição das alterações"

# Enviar alterações para o GitHub
git push origin main

Recursos Úteis:
Guia de Referência: Git Documentation.
"""
