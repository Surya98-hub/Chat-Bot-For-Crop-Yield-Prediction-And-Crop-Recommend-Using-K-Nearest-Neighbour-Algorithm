import warnings
warnings.simplefilter("ignore")

from django.shortcuts import render, redirect
from .models import Bot, mylogin
from django.http import JsonResponse
import pickle
import numpy as np
import random
import os
from django.conf import settings
import pandas as pd
import re
from django.contrib.auth import authenticate, login, logout
# import warnings

# warnings.filterwarnings("ignore", category=RuntimeWarning)
# warnings.filterwarnings("ignore", category=UserWarning)


i = 0
x = 0
crop_yield = []
crop_recommand = []
crop = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

yield_model=pickle.load(open(os.path.join(settings.BASE_DIR,'project/model/decision_tree_predict.pkl'), 'rb'))
recommand_model=pickle.load(open(os.path.join(settings.BASE_DIR,'project/model/decision tree.pkl'), 'rb'))

df1 = pd.read_excel(os.path.join('project/dataset/crop_csv_file.xlsx'))
df2 = pd.read_excel(os.path.join('project/dataset/modified_data.xlsx'))


def home(request):
    return render(request, 'chat.html')

def register(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('pass')
        reg = mylogin.objects.create(username= name, password = password)
        reg.save()
        login(request, reg)
        return render(request, 'chat.html')
     return render(request, 'reg.html')

def log(request):
     if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('pass')
        reg = authenticate(username= name, password = password) 
        print('1', name, password, reg)
        filt = mylogin.objects.get(username=name, password=password)
        print(filt)
        if filt is not None:
            login(request, filt)
            print('2')
            return render(request, 'chat.html')
     return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def bot_reply(request):
    global i
    global x
    if request.method == 'POST':
        question = request.POST.get('messageText')
        question = question.lower()
        if question in ('yield' or 'yield prediction'):
            i = +1
            return JsonResponse({'status': 'OK', 'answer': 'ok i can help you please first enter: <br><br> Your State Name'})
        elif i == 1:
            i += 1
            if 'State_Name' in df1.columns:
                target_row = df1.loc[df1['State_Name'].str.lower() == question]

                if not target_row.empty:
                    row_index = target_row.index[0]
                    column_index = target_row.columns.get_loc('State_Name')

                    value = df2.iloc[row_index, column_index]

                    print(value)
                if value == None:
                        return JsonResponse({'status': 'OK', 'answer': 'Please enter correctly'})
            crop_yield.append(int(value))
            return JsonResponse({'status': 'OK', 'answer': 'Your District Name: <br><br> Any of this: Chennai, Vellore, Chengalpattu, Coimbatore, Nilgiris, Theni, Salem, Virudhunagar, Thootukudi, Krishnagiri'})
        elif i == 2:
            i += 1
            if 'District_Name' in df1.columns:
                target_row = df1.loc[df1['District_Name'].str.lower() == question]

                if not target_row.empty:
                    row_index = target_row.index[0]
                    column_index = target_row.columns.get_loc('District_Name')

                    value = df2.iloc[row_index, column_index]

                    print(value)
                if value == None:
                        return JsonResponse({'status': 'OK', 'answer': 'Please enter correctly'})    
            crop_yield.append(int(value))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Year'})
        elif i== 3:
            i += 1
            value = random.randint(0,17)
            crop_yield.append(int(value))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Season <br><br> Any of this season: kharif, whole year, rabi, autumn,'})
        elif i == 4:
            i += 1
            if question == 'kharif':
                value = 1
            elif question == 'whole year':
                value = 3
            elif question == 'rabi':
                value = 2
            elif question == 'autumn':
                value = 0
            if value == None:
                        return JsonResponse({'status': 'OK', 'answer': 'Please enter correctly given Season'})      
            crop_yield.append(int(value))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Your Crop <br><br> Any of this: arecanut, rice, banana, coconut, sugarcane, sweet potato, cashewnut, black pepper, dry chillies'})
        elif i== 5:
            i += 1
            if question == 'arecanut':
                value = 0
            if question == 'rice':
                value = 51
            if question == 'banana':
                value = 3
            if question == 'coconut':
                value = 13
            if question == 'sugarcane':
                value = 58
            if question == 'sweet potato':
                value = 60
            if question == 'cashewnut':
                value = 41
            if question == 'black pepper':
                value = 6
            if question == 'dry chillies':
                value = 18
            if value == None:
                        return JsonResponse({'status': 'OK', 'answer': 'Please enter correctly given Crop Name'})                          
            crop_yield.append(int(value))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Temperature'})
        elif i == 6:
            i += 1
            crop_yield.append(int(question))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Humidity'})
        elif i == 7:
            i += 1
            crop_yield.append(int(question))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Your Soilmoisture'})
        elif i == 8:
            i = 10
            crop_yield.append(int(question))
            return JsonResponse({'status': 'OK', 'answer': ' Enter Your Area'})
        elif i == 10:
            i = 0
            crop_yield.append(int(question))   
            print(crop_yield)     

            crop_yields = np.array([crop_yield])    
            prediction = yield_model.predict(crop_yields)
            return JsonResponse({'status': 'OK', 'answer': 'The prediction of crop yield is: {}'.format(prediction[0])})
        
        if question in ('recommend', 'recommendation'):
            x +=1
            return JsonResponse({'status': 'OK', 'answer': 'ok i can help you please first enter: <br><br> Enter Nitrogen Value'})
        elif x == 1:
            x +=1
            crop_recommand.append(int(question))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Phosphorus Value'})
        elif x == 2:
            x +=1
            crop_recommand.append(int(question))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Potassium Value'})
        elif x == 3:
            x += 1
            crop_recommand.append(int(question))
            return JsonResponse({'status': 'OK', 'answer': 'Your Place Temperature'})
        elif x == 4:
            x +=1
            crop_recommand.append(float(question))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Humidity Value'})
        elif x == 5:
            x +=1
            crop_recommand.append(float(question))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Ph Value'})
        elif x == 6:
            x +=1
            crop_recommand.append(float(question))
            return JsonResponse({'status': 'OK', 'answer': 'Enter Your Area Rainfall'})
        elif x == 7:
            x = 0
            crop_recommand.append(float(question))
            predictions = recommand_model.predict([crop_recommand])
            predictions = '{}'.format(predictions)
            b = [int(num) for num in re.sub(r"\s+", ",", predictions.strip("[]")).split(",")]
            # b = b[0].index(1)
            space = []
            for l, d in enumerate(b):
                for i, index in enumerate(b):
                    if index == 1:
                        space.append(i)
            # print(b)
            pred_crop = crop[space[0]]
            return JsonResponse({'status': 'OK', 'answer': 'Your Land Suitable Crop Is <b>{}<b>'.format(pred_crop)})
        bot = Bot.objects.filter(user = question).values_list('bot', flat= True)
        bot = str(bot[0])
        print(bot)
        
        return JsonResponse({'status': 'OK', 'answer': bot})

    return render(request, 'chat.html')

