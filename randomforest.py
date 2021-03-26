import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA

def predict_potential(data= []):
    
    df = pd.read_csv("FIFA19.csv")
    newdf = df[['Age','Stamina', 'Strength', 'ShortPassing','LongPassing','SprintSpeed','Finishing','Overall']]
    null_check = pd.isnull(newdf)
    if pd.isnull(newdf).values.any()== True:
        newdf.fillna(newdf.mean())

    X = newdf.iloc[:, :-1].values
    Y = newdf.iloc[:,-1].values

    # train set and test set----------
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size= 0.2, random_state= 0)

    from sklearn.ensemble import RandomForestRegressor
    regressor = RandomForestRegressor(n_estimators = 50, random_state= 0)
    regressor.fit(X_train,y_train)
    y_pred = regressor.predict(X_test)
    np.set_printoptions(precision=2)
    np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1 )), 1)

    from sklearn.metrics import r2_score
    r_square = r2_score(y_test, y_pred)


    predicted_potential = regressor.predict([data])
    return predicted_potential

def recommend_player(player):
    df1 = pd.read_csv("FIFA19.csv")
    df2 = pd.read_csv("FIFA19.csv")
    
    attr = df2.iloc[:, 21:-3]
    attr['Skill Moves'] = df2['Skill Moves']
    workrate = df2['Work Rate'].str.get_dummies(sep='/ ')
    attr = pd.concat([attr, workrate], axis=1)
    df2 = attr
    attr = attr.dropna()
    df2['Name']  = df1["Name"]
    df2 = df2.dropna()
    # Running the classification KNN model*****
    scaled = StandardScaler()
    X = scaled.fit_transform(attr)
    classifier = NearestNeighbors(n_neighbors=6,algorithm='ball_tree')
    classifier.fit(X)
    player_index = classifier.kneighbors(X)[1]


    print("5 Players similar to {} are : ".format(player))
    index =  df2[df2['Name'] == player].index.tolist()[0]
    for i in player_index[index][1:]:
        print(df2.iloc[i]['Name'])



