import os
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import sklearn.externals
import joblib
# from keras.models import Sequential
# from keras.layers import Dense,Activation,Flatten
from sklearn.preprocessing import MinMaxScaler
import warnings


async def testCSV(start,end):
    warnings.filterwarnings('ignore')# load the model from disk
    #df = pd.read_csv(file.file,  parse_dates=[0], header=None,index_col=0, squeeze=True,names=['Fecha','Mañana','Tarde'])
    #dfm=df[['Mañana']]
    #print(dfm)
    #dft=df[['Tarde']]
    #print(dft)

    filename_m=os.path.abspath("models/model_221009.pkl")
    filename_t=os.path.abspath("models/model_221009t.pkl")
    model_m = joblib.load(filename_m)
    model_t = joblib.load(filename_t)
    #VALOR QUE INGRESA A LA API POR EL CLIENTE UN PARAMETRO START Y OTRO END
    index_future = pd.date_range(start,end)
    print(index_future)
    predm= model_m.predict(start=1328,end=1328+7,typ='levels')
    predm.index = index_future
    predt= model_t.predict(start=1328,end=1328+7,typ='levels')
    predt.index = index_future

    result = {}
    for i,v in predm.items():
       result[i.strftime("%Y-%m-%d")] ={'Morning':v,'Aftermoon':v}
    for i,v in predt.items():
       result[i.strftime("%Y-%m-%d")]['Aftermoon'] = v
    return result