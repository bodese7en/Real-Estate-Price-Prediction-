import pickle
import json
import numpy as np

__district = None
__data_columns = None
__model = None

def predict_home_price(rooms,size,level,district):
    try:
        loc_index = __data_columns.index(district.lower())
    except:
        loc_index = -1    

    x = np.zeros(len(__data_columns))
    x[0] = rooms
    x[1] = size
    x[2] = level
    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict([x])[0],0)

def load_saved_artefacts():
    print("loading saved artefacts...start")
    global  __data_columns
    global __district
    global __model

    if __model is None:
        with open('server/artefacts/real_estate_model.pickle', 'rb') as f:
            __model = pickle.load(f)
            print("loading saved artefacts...done")

    if __data_columns is None:
        with open("server/artefacts/columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']
            __district = __data_columns[3:]

def get_data_columns():
    return __data_columns

def get_location_names():
    return __district

if __name__ == '__main__':
    load_saved_artefacts()
    print(get_location_names())
    print(predict_home_price(3,68,4,'Yakkasaroy')) #testing the model
    print(predict_home_price(2,128,2,'Mirobod'))

