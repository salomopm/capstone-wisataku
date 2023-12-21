from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
import pandas as pd



popular_df = pd.read_hdf('popular.h5', key='data')
pt = pd.read_hdf('pt.h5', key='data')
info_tourism = pickle.load(open('info_tourism.pkl','rb'))
cosine_sim = pickle.load(open('cosine_sim.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():

    return jsonify(
                           place_name = list(popular_df['Place_Name'].values),
                           description=list(popular_df['Description'].values),
                           votes=list(map(float, popular_df['num_ratings'].values)),
                           rating=list(map(float, popular_df['avg_rating'].values))
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')

@app.route('/recommend_Place',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    cosine_items = sorted(list(enumerate(cosine_sim [index])), key=lambda x: x[1], reverse=True)[1:21]

    data = []
    for i in cosine_items:
        item = []
        temp_df = info_tourism[info_tourism['Place_Name'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Place_Name')['Place_Name'].values))
        item.extend(list(temp_df.drop_duplicates('Place_Name')['City'].values))
        item.extend(list(temp_df.drop_duplicates('Place_Name')['Description'].values))
        item.extend(list(temp_df.drop_duplicates('Place_Name')['Category'].values))
        item.extend(list(map(float, temp_df.drop_duplicates('Place_Name')['Price'].values)))
        item.extend(list(map(float, temp_df.drop_duplicates('Place_Name')['avrg_rating'].values)))
        data.append(item)

    print(data)

    return jsonify(data=data)

if __name__ == '__main__':
    app.run(debug=True)