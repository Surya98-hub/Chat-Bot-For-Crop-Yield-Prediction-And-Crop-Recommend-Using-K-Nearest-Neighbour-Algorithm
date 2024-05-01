# import pickle

# crop_yield = [1,5,5,3,40,37,40,46,1359.0]
# print(crop_yield)
# with open('model/decision_tree.pkl', "rb") as file:
#                 model = pickle.load(file)
# prediction = model.predict([crop_yield])

# import pickle
# import numpy as np
#                     #    [1, 5, 5, 3, 40, 37, 40, 46]
# crop_yield = np.array([[1, 5, 5, 3, 40, 37, 40, 46, 1359]])  # Provide the input as a numpy array
# print(crop_yield)

# with open('model/decision_tree.pkl', "rb") as file:
#     model = pickle.load(file)

# prediction = model.predict(crop_yield)
# print(prediction,'i am a output')

# import pandas as pd

# df1 = pd.read_excel('crop_csv_file.xlsx')
# print(df1.head())

# if 'season' in df1.columns:
#     target_row = df1.loc[df1['season'].str.lower() == 'Kharif ']
#     print(target_row, '1........')
#     if not target_row.empty:
#         row_index = target_row.index[0]
#         column_index = target_row.columns.get_loc('season')
#         print(row_index, column_index, '2........')

#         df2 = pd.read_excel('modified_data.xlsx')


#         value = df2.iloc[row_index, column_index]

#         print(value)

import re
import pandas as pd
import pickle
import numpy

crop = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

# Load the pickle file
# RF_pkl_filename = 'model/Decision tree.pkl'
# with open(RF_pkl_filename, 'rb') as file:
#     loaded_model = pickle.load(file)


# predictions = loaded_model.predict( [[38, 14, 30, 26.924495, 91.201060, 5.570745, 194.902214]])
# print(predictions)
a = '[[0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]]'
c = '{}'.format(a)
b = [int(num) for num in re.sub(r"\s+", ",", c.strip("[]")).split(",")]
# b = [int(num) for num in re.sub(r"\s+", ",", predictions.strip("[]")).split(",")]
# b = str(b[0]).index(1)
space = []
for x, d in enumerate(b):
    for i, index in enumerate(b):
        if index == 1:
            space.append(i)
print(b)
print(space)
# pred_crop = crop[b]
# print(pred_crop)
