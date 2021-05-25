from django.shortcuts import render
from django_pandas.io import read_frame # this
from users.models import UserProfile
import pandas as pd


def menu_index(request):
    print("********************************")
    df=pd.read_excel(r"C:\diet\dietproj\menu\projectfood1.xlsx")
    print(df.iloc[1])
    meal={}
    meal['title']=(df.iloc[1]['name'])
    meal['cals']=(df.iloc[1]['cals'])
    meal['pic']=(df.iloc[1]['pic'])
    profile=UserProfile.objects.get(user=request.user)
    bmi=profile.bmi()
    maxcal=profile.maxcal()
    print (bmi)
    print(maxcal)
    context={'meal':meal,'bmi':bmi,'maxcal':maxcal}
    print(context)
    return render(request, 'menu_index.html' , context)

def menu_detail(request, pk):
    return render(request, 'menu_detail.html')