#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[314]:


import pandas as pd
import numpy as np


# In[315]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[10]:


black_friday.shape


# In[7]:


black_friday.info()


# In[8]:


black_friday.describe()


# In[4]:


black_friday.head()


# In[5]:


black_friday['Gender'].value_counts()


# In[6]:


black_friday['Age'].value_counts()


# In[9]:


black_friday['Marital_Status'].value_counts()


# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[134]:


def q1():
    return black_friday.shape
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar. SEM CONSIDERAR `User_ID` únicos

# In[297]:


def q2():
    return int(black_friday[black_friday['Age']=='26-35'].groupby('Gender')['User_ID'].count()['F'])
    # q2 = black_friday[black_friday['Age']=='26-35']
    # q2[q2['Gender']=='M']['User_ID'].nunique()
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[135]:


def q3():
    return black_friday['User_ID'].nunique()
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[137]:


def q4():
    return black_friday.dtypes.nunique()
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[299]:


def q5():
    return float(black_friday.isna().sum().max()/black_friday.shape[0])
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[301]:


def q6():
    return int(black_friday.isnull().sum().max())
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[203]:


def q7():
    return black_friday['Product_Category_3'].mode().iloc[0]
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[280]:


def q8():
    return float(((black_friday['Purchase'] - black_friday['Purchase'].min()) / (black_friday['Purchase'].max() - black_friday['Purchase'].min())).mean())
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[325]:


def q9():
    mean = black_friday['Purchase'].mean()
    std = black_friday['Purchase'].std()
    black_friday['Purchase_std'] = (black_friday['Purchase'] - mean) / std
    return int(black_friday['Purchase_std'].between(-1,1).value_counts()[True])
    # OU black_friday['Purchase_std'].between(-1,1).value_counts().iloc[0]
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[356]:


def q10():
    return bool(black_friday[black_friday['Product_Category_2'].isna() & black_friday['Product_Category_3'].isna()].shape[0] == black_friday['Product_Category_2'].isna().sum())
    pass

