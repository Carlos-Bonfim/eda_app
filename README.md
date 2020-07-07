# eda_app
App para ter rapidamente as primeiras impressões de um conjunto de dados.

Com este app você poderá, sem precisar digitar uma linha de código:
1. Ter um tutorial básico sobre `Análise Exploratória de dados`;
2. Visualizar as primeiras linhas do seu *dataset*;
3. Verificar os tipos de dados, assim como suas quantidades de linhas e colunas;
4. Verificar se há dados faltantes e sua porcentagem;
5. Analisar as principais estatísticas resumidamente;
6. selecionar o tipo de dados:
- Variáveis numéricas: 
   - Histograma: escolher qual *feature* quer analisar, assim como coeficiente de *kurtosis* e *skewness*.
   - Correlação: escolher as variáveis x e y para analisar em um *scatterplot* assim como seu coeficiente.
- Variáveis categóricas:
   - Analise um gráfico de barras.


## Como utilizar
Para rodar em um computador local:
1. Coloque os arquivos na mesma pasta;
2. Abra o terminal;
3. Entre no diretório dos arquivos;
4. entre com o comando: *streamlit run eda_app.py*

O app abrirá em uma página do seu navegador.

Arraste um arquivo .csv para o local indicado e analise os dados.

Na pasta *dados* aqui do repositório tem um arquivo para teste, caso desejar.
