from django.shortcuts import render
import os


def index(request):
    wd = os.getcwd()
    print(wd)
    wd = wd + '\\static\\assets\\'
    list1 = os.listdir(wd + 'company')
    list2 = os.listdir(wd + 'product')
    list1 = ['assets\\company\\' + i for i in list1]
    list2 = ['assets\\product\\' + i for i in list2]
    print(list2)
    params = {"listcompany": list1, 'listProducts': list2}
    return render(request, 'Home/index.html', params)


def about(request):
    return render(request, 'Home/about.html')
