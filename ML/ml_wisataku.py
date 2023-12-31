# -*- coding: utf-8 -*-
"""ML_WisataKu.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dkAEDL46IVCqJLF2uxaI4aEqFHVh5-Lc

# Dataset Collection
"""

from google.colab import files

uploaded = files.upload()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


info_tourism = pd.read_csv("tourism_with_id.csv")
tourism_rating = pd.read_csv("tourism_rating.csv")
users = pd.read_csv("user.csv")

info_tourism.info()

tourism_rating.info()

users.info()

print(f"Jumlah tempat wisata dalam Data : {len(info_tourism.Place_Id.unique())}")
print(f"Jumlah user : {len(users.User_Id.unique())}")
print(f"Jumlah rating yang diberikan user pada Data : {len(tourism_rating.User_Id)}")

info_tourism.head()

users.head()

tourism_rating.head()

plt.title('City')
info_tourism.City.value_counts().plot(kind='barh', color='g');

plt.title('Category')
info_tourism.Category.value_counts().plot(kind='barh', color='y')

plt.title('Price')
info_tourism.Price.value_counts().plot(kind='barh', color='r')

plt.title('avrg_rating')
info_tourism.avrg_rating.value_counts().plot(kind='barh', color='b')

info_tourism.sample(10)

tourism_rating.sample(10)

users.sample(10)

"""# Data Pre-Processing"""

total_tourism = np.concatenate((
info_tourism.Place_Id.unique(),
tourism_rating.Place_Id.unique()
))

total_tourism = np.sort(np.unique(total_tourism))
print(f"Jumlah total tempat wisata: {len(total_tourism)}")

ratings_with_name = tourism_rating.merge(info_tourism,on='Place_Id')

total_tourism_rate = ratings_with_name
total_tourism_rate

num_rating_df = ratings_with_name.groupby('Place_Name').count()['Place_Ratings'].reset_index()
num_rating_df.rename(columns={'Place_Ratings':'num_ratings'},inplace=True)
num_rating_df

avg_rating_df = ratings_with_name.groupby('Place_Name').mean()['Place_Ratings'].reset_index()
avg_rating_df.rename(columns={'Place_Ratings':'avg_rating'},inplace=True)
avg_rating_df

total_tourism = pd.merge(total_tourism_rate,info_tourism[["Place_Id"]],on='Place_Id', how='left')
total_tourism

total_tourism['city_category'] = total_tourism[['City','Category']].agg(' '.join,axis=1)
total_tourism

"""# Data Preparation"""

total_tourism.isnull().sum()

info_tourism.isna().sum()

tourism_rating.isna().sum()

users.isna().sum()

preparation = total_tourism.drop_duplicates("Place_Id")
preparation

place_id = preparation.Place_Id.tolist()
place_name = preparation.Place_Name.tolist()
place_avg_rating = preparation.avrg_rating.tolist()
place_category = preparation.Category.tolist()
place_desc = preparation.Description.tolist()
place_city = preparation.City.tolist()
price = preparation.Price.tolist()
city_category = preparation.city_category.tolist()

new_tourism = pd.DataFrame({
    "Place ID":place_id,
    "Place_Name":place_name,
    "Category":place_category,
    "Description":place_desc,
    "Average Rating":place_avg_rating,
    "Price":price,
    "City":place_city,
    "City Category":city_category
})

new_tourism

top_20 = new_tourism['Place ID'].value_counts().reset_index()[0:20]
top_20 = pd.merge(top_20,preparation[['Place_Id','Place_Name']], how='left', left_on='index', right_on='Place_Id')

# Visualisasi wisata berdasarkan jumlah rating terbanyak
plt.figure(figsize=(7,5))
sns.barplot(x='Place_Id', y='Place_Name', data = top_20)
plt.title('Jumlah Tempat Wisata dengan Rating Terbanyak', pad=20)
plt.xlabel('Jumlah Rating')
plt.ylabel('Nama Lokasi')
plt.show()

sns.countplot(y='Category', data=preparation)
plt.title('Perbandingan Jumlah Kategori Wisata', pad=20)
plt.show()

asal_kota = users['Location'].apply(lambda x : x.split(',')[0])

# Visualisasi asal kota user
plt.figure(figsize=(8,6))
sns.countplot(y=asal_kota)
plt.title('Jumlah Asal Kota User')
plt.show()

"""# Model Rekomendasi"""

import pandas as pd
import numpy as np
from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt
from tensorflow.keras.models import save_model

data = new_tourism
data.sample(10)

from sklearn.datasets import load_iris

iris = load_iris()

X, y = iris.data, iris.target

print(X[:5])
print(y[:5])

df = pd.DataFrame(iris.data, columns=iris.feature_names)

df.head()

# Term Frequency-Inverse Document Frequency (TF-IDF)

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()

cv.fit(data['City Category'])

print("Features Name: ", list(cv.vocabulary_.keys()))

cv_matrix = cv.transform(data['City Category'])

cv_matrix.shape

cv_matrix.todense()

total_tourism.head()

x = total_tourism.groupby('city_category').count()['avrg_rating'] > 0
padhe_likhe_users = x[x].index

filtered_rating = total_tourism[total_tourism['city_category'].isin(padhe_likhe_users)]

y = filtered_rating.groupby('Place_Name').count()['avrg_rating']>=0
famous_places = y[y].index

final_ratings = filtered_rating[filtered_rating['Place_Name'].isin(famous_places)]

pt = final_ratings.pivot_table(index='Place_Name',columns='city_category',values='avrg_rating')
pt.fillna(0,inplace=True)

pt

#Cosine

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(pt)

cosine_sim.shape

# Model Recomendation

def tourism_recommendations(new_tourism):

   # index fetch

    index = np.where(pt.index==new_tourism)[0][0]
    similar_items = sorted(list(enumerate(cosine_sim[index])),key=lambda x:x[1],reverse=True)[1:12]

    data = []
    for i in similar_items:
        item = []
        temp_df = info_tourism[info_tourism['Place_Name'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Place_Name')['Place_Name'].values))
        item.extend(list(temp_df.drop_duplicates('Place_Name')['Description'].values))
        item.extend(list(temp_df.drop_duplicates('Place_Name')['Category'].values))
        item.extend(list(temp_df.drop_duplicates('Place_Name')['City'].values))
        item.extend(list(temp_df.drop_duplicates('Place_Name')['Price'].values))
        item.extend(list(temp_df.drop_duplicates('Place_Name')['avrg_rating'].values))

        data.append(item)

    recommendations = pd.DataFrame(data, columns=['Place_Name', 'Description', 'Category', 'City', 'Price','avrg_rating'])
    return recommendations

tourism_recommendations("Air Mancur Menari")

tourism_recommendations("Candi Ratu Boko")

df = tourism_rating
df

pt.index[48]

user_ids = df.User_Id.unique().tolist()

user_to_user_encoded = {x:i for i, x in enumerate(user_ids)}

user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}

place_ids = df.Place_Id.unique().tolist()

place_to_place_encoded = {x: i for i, x in enumerate(place_ids)}

place_encoded_to_place = {x: i for x, i in enumerate(place_ids)}

df['user'] = df.User_Id.map(user_to_user_encoded)

df['place'] = df.Place_Id.map(place_to_place_encoded)

num_users = len(user_to_user_encoded)

num_place = len(place_encoded_to_place)

df['Place_Ratings'] = df['Place_Ratings'].values.astype(np.float64)

min_rating = min(df['Place_Ratings'])

max_rating= max(df['Place_Ratings'])

print('Number of User: {}, Number of Place: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_place, min_rating, max_rating
))

# Train and Test Model

df = df.sample(frac=1,random_state=42)
df

x = df[['user','place']].values

y = df['Place_Ratings'].apply(lambda x:(x-min_rating)/(max_rating-min_rating)).values

train_indices = int(0.8 * df.shape[0])

x_train,x_val,y_train,y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x,y)

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_place, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_place = num_place
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding(
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1)
    self.place_embedding = layers.Embedding(
        num_place,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.place_bias = layers.Embedding(num_place, 1)

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    place_vector = self.place_embedding(inputs[:, 1]) # memanggil layer embedding 3
    place_bias = self.place_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_place = tf.tensordot(user_vector, place_vector, 2)

    x = dot_user_place + user_bias + place_bias

    return tf.nn.sigmoid(x) # activation sigmoid

model = RecommenderNet(num_users, num_place, 50)

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('val_root_mean_squared_error')<0.2):
      print('Metriks validasi sudah baik')
      self.model.stop_training = True

history = model.fit(
    x = x_train,
    y = y_train,
    epochs = 100,
    validation_data = (x_val, y_val),
    callbacks = [myCallback()]
)

model.save('saved_model.pkl')

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.ylim(ymin=0, ymax=0.4)
plt.legend(['train', 'test'], loc='center left')
plt.show()

import pickle

pickle.dump(info_tourism,open('info_tourism.pkl','wb'))
pickle.dump(cosine_sim,open('cosine_sim.pkl','wb'))

pt.to_hdf('pt.h5', key='data', mode='w')

"""# Model Top 10

"""

ratings_with_name = tourism_rating.merge(info_tourism, on='Place_Id')

num_rating_df = ratings_with_name.groupby('Place_Name').count()['Place_Ratings'].reset_index()
num_rating_df.rename(columns={'Place_Ratings':'num_ratings'},inplace=True)
num_rating_df

avg_rating_df = ratings_with_name.groupby('Place_Name').mean()['Place_Ratings'].reset_index()
avg_rating_df.rename(columns={'Place_Ratings':'avg_rating'},inplace=True)
avg_rating_df

popular_df = num_rating_df.merge(avg_rating_df,on='Place_Name')
popular_df

popular_df = popular_df[popular_df['num_ratings']>=0].sort_values('avg_rating',ascending=False).head(10)
popular_df = popular_df.merge(info_tourism,on='Place_Name').drop_duplicates('Place_Name')[['Place_Id','Place_Name','Description','Category','City','Price','num_ratings','avg_rating']]

print('Daftar Rekomendasi dari User')
print('===' * 9)
print('Tempat wisata dengan rating tertinggi dari user')

print('----' * 8)
print('Top 10 place recommendation')
print('----' * 8)
popular_df

popular_df.to_hdf('popular.h5', key='data', mode='w')

"""# Load Model

"""