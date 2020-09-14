#!/usr/bin/env python
# coding: utf-8

# In[11]:



import numpy as np


# task 1 Создайте массив Numpy под названием a размером 5x2, то есть состоящий из 5 строк и 2 столбцов. Первый столбец должен содержать числа 1, 2, 3, 3, 1, а второй - числа 6, 8, 11, 10, 7. Будем считать, что каждый столбец - это признак, а строка - наблюдение. Затем найдите среднее значение по каждому признаку, используя метод mean массива Numpy. Результат запишите в массив mean_a, в нем должно быть 2 элемента.

# In[6]:


a = np.array([1, 6, 2, 8, 3, 11, 3, 10, 1, 7]).reshape(5, 2) 


# In[7]:


a


# In[8]:


mean_a = a.mean(axis = 0)


# In[9]:


mean_a


# task 2 Вычислите массив a_centered, отняв от значений массива “а” средние значения соответствующих признаков, содержащиеся в массиве mean_a. Вычисление должно производиться в одно действие. Получившийся массив должен иметь размер 5x2.

# In[10]:


a_centered = a - mean_a


# In[11]:


a_centered


# task 3 Найдите скалярное произведение столбцов массива a_centered. В результате должна получиться величина a_centered_sp. Затем поделите a_centered_sp на N-1, где N - число наблюдений.

# In[12]:


a_centered_sp = np.dot(a_centered[:, 0], a_centered[:, 1])


# In[13]:


a_centered_sp


# In[14]:


a_centered_sp / (a.shape[0] - 1)


# Pandas

# In[12]:


import pandas as pd
import numpy as np


# task 1 Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные: 
# [1, 1, 1, 2, 2, 3, 3], 
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].
# 

# In[16]:


import pandas as pd
import numpy as np


# In[17]:


authors = pd.DataFrame({'author_id': [1, 2, 3], 'author_name': ['Тургенев', 'Чехов', 'Островский']}, columns = ['author_id', 'author_name'])


# In[18]:


authors


# In[24]:


book = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3], 'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'], 'price': [450, 300, 350, 500, 450, 370, 290]}, columns = [ 'author_id', 'book_title', 'price'])
book


# task 2 
# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id.
# 

# In[30]:


authors_price = pd.merge(authors, book, on = 'author_id', how = 'inner')
authors_price


# task 3 Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

# In[32]:


top5 = authors_price.nlargest(5, 'price')
top5


# In[ ]:





# task 4 Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора,минимальная, максимальная и средняя цена на книги этого автора.
# 

# In[39]:


authors_stat = authors_price.groupby('author_name')['price'].agg(['min', 'max', 'mean']).reset_index()


# In[40]:


authors_stat 


# In[41]:


authors_stat = authors_stat.rename(columns = {'min': 'min_price', 'max': 'max_price ', 'mean':'mean_price'})
authors_stat


# In[ ]:




