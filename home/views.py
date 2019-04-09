from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from . import movie_recommender

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def search(request):
    form = forms.SearchForm()

    if request.method == 'POST':
        form = forms.SearchForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            flag = movie_recommender.look_for(title)
            
            if(flag==False):
                print("Movie not found in the database")
            else:
                r_list = movie_recommender.get_recommendation(title)
                print(r_list)


    return render(request, 'home/search_page.html',{"form":form,})
