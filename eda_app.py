import pandas as pd
import numpy as np
import plotly.express as px
from scipy.stats import kurtosis, skew
import streamlit as st


def main():

    st.sidebar.image('icon_images/icon-logo.png', width=300)
    st.sidebar.header('Selecione uma opção')
    opt = st.sidebar.radio('',(['Conceito sobre EDA','Seu conjunto de dados']))

    st.title('ANÁLISE EXPLORATÓRIA DE DADOS')

    if opt == 'Conceito sobre EDA':
        st.subheader('Conceito')
        st.write("""
        `Análise Exploratória de dados` ou em inglês (*EDA – Exploratory Data Analysis*) é um estado da 
        mente e não um conjunto de regras pré-estabelecidas. Nesta fase você fica livre para investigar qualquer 
        ideia que surgir.  
        Esta etapa é muito importante quando se fala em `análise de dados`, pois a partir dela você gera 
        **insights** e com base nisso você desenvolverá todo o restante, para cumprir seu objetivo. É um ciclo 
        iterativo.
        """)
        st.image('icon_images/ciclo_eda.png')

        st.subheader('Questões')
        st.write("""
        O principal objetivo é `entender seus dados`. Um jeito mais fácil é `fazer perguntas` para guiar 
        seu entendimento, pois com isso você foca sua atenção em algo específico.  
        EDA é um processo criativo e a *chave* para criar perguntas de qualidade é `criar um monte de perguntas`, 
        porque não sabemos, logo de cara, quais **insights** contém nossos dados. É difícil você ter algo 
        “*matador*” no início, mas conforme você irá respondendo essas perguntas, outras vão surgindo e com isso 
        suas `descobertas` vão aumentando.
        
        O **importante é guiar sua pesquisa**. Contudo, dois tipos de perguntas mostram alguns caminhos para 
        descobertas nos seus dados:  
            **1.** *Que tipo de variação ocorre com minhas variáveis?*  
            **2.** *Que tipo de co-variação ocorre entre minhas variáveis?*
        
        Antes de continuar, vamos definir alguns termos:
        - `Variável:` é uma quantidade, qualidade, ou algo a ser medido.
        - `Valor:` é o estado da variável quando medida.
        - `Observação:` é o conjunto de medidas feitas sobre uma condição similar.
        - `Dados tabulares:` é um conjunto de valores associados com uma variável e uma observação. Os dados 
        em forma tabular são organizados em lugares como, células, que é o cruzamento de uma variável, que são 
        as colunas e as observações que são as linhas.
        
        Em um mundo perfeito, os dados ficam organizados, mas na vida real nem sempre é assim e geralmente nós 
        temos que fazer esse trabalho "sujo".
        """)

        st.subheader('Variação')
        st.write("""
        É a tendência dos valores das variáveis mudarem de medição para medição. Uma varíavel contínua medida 
        duas vezes, dará resultados diferentes, ficando próximos um do outro. Em cada medição ocorre um padrão 
        de erro associado que varia em cada medida. Assim também, as variáveis categóricas também variam em 
        relação à diferentes fatores como cores de um objeto, por exemplo.
        
        **Toda variável carrega um padrão de variação, que pode ser uma informação importante e a melhor forma para 
        entender essa variação é visualizar as distribuições de suas variáveis.**
        
        Vamos entender um pouco sobre as variáveis e seus tipos.  
        
        São definidos da seguinte forma:
        """)
        st.image('icon_images/data_types.png')

        st.markdown('Referência: https://r4ds.had.co.nz/exploratory-data-analysis.html')

    if opt == 'Seu conjunto de dados':

        st.subheader('Importar o dataset')
        file = st.file_uploader('Arraste ou selecione a base de dados (.csv)', type='csv')
        st.markdown('*Obtenha as primeiras impressões do seu conjunto de dados.*')


        if file is not None:
            try:
                df = pd.read_csv(file).drop(['Unnamed: 0'], axis=1)
            except:
                df = pd.read_csv(file)

            st.markdown(f"Seu conjunto de dados possui **{df.shape[0]} linhas** e **{df.shape[1]} colunas**")
            st.subheader('Visualize as primeiras linhas do seu conjunto de dados')

            st.write("""
            Se seu conjunto possui muitas linhas, visualize as primeiras 5 linhas para conhecê-los, com isso 
            temos as primeiras impressões e ter uma idéia dos tipos de dados que estamos lidando.
            """)

            st.write(df.head())

            st.subheader('Visualize as últimas linhas do seu conjunto de dados')

            st.write("""
            Assim como as primeiras, visualize também as últimas linhas do seu conjunto de dados.
            """)

            st.write(df.tail())

            st.subheader('Verifique os tipos dos dados')
            st.write("""
            Saber o tipo dos dados que você está trabalhando é muito importante e com isso é possível 
            escolher a melhor abordagem para cada tipo.
            """)
            st.write(pd.DataFrame(df.dtypes).rename(columns={0:'type'}))

            st.subheader('Verifique os dados faltantes')
            st.write("""
            Lidar com dados faltantes é uma tarefa que exige muita cautela, pois qualquer transformação 
            que fizer no conjunto de dados podem gerar resultados inesperados, a quantidade de dados assim 
            como saber com qual variável está trabalhando, fará que você tome decisões mais acertivas, remover 
            a variável, *imputar* dados com valores da média, mediana, ou manter com um outro valor, pois 
            por algum motivo eles estão dispostos desta forma.
            """)
            miss_check = df.isna().mean()
            st.write(miss_check)

            st.markdown(f'Temos {miss_check.sum():.2f}% de dados faltando.')

            st.sidebar.header('Visualização')
            opt_visual = st.sidebar.radio('Selecione o tipo de dados', ['Numéricos', 'Categóricos'])

            num_list = df.select_dtypes(np.number).columns.tolist()
            cat_list = df.select_dtypes('object').columns.tolist()

            st.subheader('Analisando algumas estatísticas numéricas')
            st.write("""
            Um breve resumo sobre as principais estatísticas do seu conjunto de dados.
            """)
            st.write(df.describe().T)

            st.subheader('Analisando algumas estatísticas categóricas')
            st.write("""
            Assim como as estatísticas numéricas, podemos dar uma olhada também nas estatísticas categóricas.
            """)
            st.write(df.describe(include=['O']).T)

            if opt_visual == "Numéricos":

                st.sidebar.subheader('Histograma')
                st.subheader('Histograma')
                st.write("""
                Também é conhecido como `gráfico da Distribuição de frequências` com o objetivo de mostrar como uma determinada 
                amostra ou população está distribuída, ou seja, mede a quantidade de vezes que o valor aparece 
                dentro de uma classe. É uma das `7 ferramentas da qualidade` tendo aplicação em diversos setores.
                """)
                opt_num = st.sidebar.selectbox('Analise a distribuição de uma variável ', num_list)
                fig = px.histogram(df, x=opt_num, marginal="box")
                st.write(fig)

                coef_skew = skew(df[opt_num])
                coef_kurt = kurtosis(df[opt_num])
                st.sidebar.markdown(f'Coeficiente de kurtosis: **{coef_skew :.2f}**')
                st.sidebar.markdown(f'Coeficiente de Skewness: **{coef_kurt :.2f}**')

                st.sidebar.subheader('Correlação')

                st.sidebar.markdown("Selecione duas variáveis para analisar a correlação")
                opt_x = st.sidebar.selectbox('selecione o eixo x (variável dependente)', num_list)
                opt_y = st.sidebar.selectbox('selecione o eixo y (variável independente)', num_list)

                st.subheader('Diagrama de Dispersão ou Correlação')
                st.write("""
                É utilizado para `mostrar a relação, de forma gráfica, entre duas variáveis` em um mesmo 
                processo, mostrando que se uma variável alterar a outra também altera, ou não.  
                Com isso podemos verificar também o `coeficiente de correlação`, podendo comprovar se a 
                correlação entre essas duas variáveis é forte, média, fraca ou sem nenhuma correlação.  
                **Vale ressaltar que, mesmo duas variáveis estando correlacionadas, essa correlação não implica 
                em causalidade**.
                """)
                fig_scatter = px.scatter(df, x=opt_x, y=opt_y, trendline="ols")
                st.write(fig_scatter)
                correl = df[opt_x].corr(df[opt_y])


                st.markdown(f"A correlação entre **{opt_x}** e **{opt_y}** equivale à **{correl :.2f}**")
                if correl == 1.0:
                    st.markdown("**Correlação perfeita**")
                elif (correl >= 0.75) & (correl < 1.0):
                    st.markdown("**Correlação forte**")
                elif (correl >= 0.50) & (correl < 0.75):
                    st.markdown("**Correlação média**")
                elif (correl >= 0.25) & (correl < 0.50):
                    st.markdown("**Correlação fraca**")
                elif (correl >= 0) & (correl < 0.25):
                    st.markdown("**Correlação inexistente**")
                elif (correl >= -0.25) & (correl < 0.0):
                    st.markdown("**Correlação inexistente**")
                elif (correl >= -0.50) & (correl < -0.25):
                    st.markdown("**Correlação fraca**")
                elif (correl >= -0.75) & (correl < -0.50):
                    st.markdown("**Correlação média**")
                elif (correl >= -1.0) & (correl < -0.75):
                    st.markdown("**Correlação forte**")
                else:
                    st.markdown("**Correlação perfeita**")

            else:
                st.sidebar.subheader('Barplot')
                opt_cat = st.sidebar.selectbox('selecione qual variável analisar', cat_list)
                fig_bar = px.bar(x=df[opt_cat].value_counts().index, y=df[opt_cat].value_counts().values,
                                 title='Bar chart')
                st.write(fig_bar)



if __name__ == "__main__":
    main()