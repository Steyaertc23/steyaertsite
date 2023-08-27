from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import MovieList
from .forms import AddMovie
from random import sample


# Create your views here.
def home(response):
    return render(response, "moviesdb/home.html", {})

@login_required(login_url='/login')
def db(response):
    return render(response, 'moviesdb/db.html', {})

@login_required(login_url='/login')
def g(response):
    list = MovieList.objects.all()[0]
    movies = list.movie_set.filter(rating='G').order_by('title')
    movie_list = []
    for movie in movies:
        movie_list.append(movie.title)
    ctx = {'titles':movie_list}
    return render(response, 'moviesdb/g.html', ctx)

@login_required(login_url='/login')
def pg(response):
    list = MovieList.objects.all()[0]
    movies = list.movie_set.filter(rating='PG').order_by('title')
    movie_list = []
    for movie in movies:
        movie_list.append(movie.title)
    ctx = {'titles':movie_list}
    return render(response, 'moviesdb/pg.html', ctx)

@login_required(login_url='/login')
def pg13(response):
    list = MovieList.objects.all()[0]
    movies = list.movie_set.filter(rating='PG-13').order_by('title')
    movie_list = []
    for movie in movies:
        movie_list.append(movie.title)
    ctx = {'titles':movie_list}
    return render(response, 'moviesdb/pg13.html', ctx)

@login_required(login_url='/login')
def r(response):
    list = MovieList.objects.all()[0]
    movies = list.movie_set.filter(rating='R').order_by('title')
    movie_list = []
    for movie in movies:
        movie_list.append(movie.title)
    ctx = {'titles':movie_list}
    return render(response, 'moviesdb/r.html', ctx)

@login_required(login_url='/login')
def nr(response):
    list = MovieList.objects.all()[0]
    movies = list.movie_set.filter(rating='NR').order_by('title')
    movie_list = []
    for movie in movies:
        movie_list.append(movie.title)
    ctx = {'titles':movie_list}
    return render(response, 'moviesdb/nr.html', ctx)

@login_required(login_url='/login')
def tv(response):
    list = MovieList.objects.all()[0]
    movies = list.movie_set.filter(rating='TV').order_by('title')
    movie_list = []
    for movie in movies:
        movie_list.append(movie.title)
    ctx = {'titles':movie_list}
    return render(response, 'moviesdb/tv.html', ctx)

@login_required(login_url='/login')
def add(response):
    if response.method == 'POST':
        form = AddMovie(response.POST)

        if form.is_valid():
            t = form.cleaned_data['title']
            r = form.cleaned_data['rating']
            d = form.cleaned_data['disk']

            ls = MovieList.objects.get(name='Steyaert Movie Database')
            ls.movie_set.create(title=t, rating=r, disk=d)
            return HttpResponseRedirect('/db')
    else:
        form = AddMovie()
    return render(response, 'moviesdb/add.html', {'form':form})

@login_required(login_url='/login')
def search(response):
    return render(response, 'moviesdb/search.html', {})

@login_required(login_url='/login')
def search_results(response):
    title = response.GET.get('title')
    if not title == 'Title':
        ml = MovieList.objects.all()[0]
        titles = ml.movie_set.all()
        temp = []
        for t in titles:
            movie_title = t.title.lower()

            if title.lower() in movie_title:
                temp.append(t)
        titles = temp
        if not len(titles) == 0:

            ctx = {'titles':titles, 't':title}
        else:
            ctx = {'titles':[f'There are no titles that match the query "{title}"'], 't':title}
    else:
        return HttpResponseRedirect('/search')
    return render(response, 'moviesdb/searchRes.html', ctx)

@login_required(login_url='/login')
def random(response):
    return render(response, 'moviesdb/random.html', {})

def good_num(num:str):
    try:
        x = int(num)
        if x > 10:
            x = 10
        if x < 1: 
            x = 1
        return x
    except:
        x = 1
        return x

@login_required(login_url='/login')
def random_results(response):
    g = response.GET.get('g') == 'on'
    pg = response.GET.get('pg') == 'on'
    pg13 = response.GET.get('pg13') == 'on'
    r = response.GET.get('r') == 'on'
    nr = response.GET.get('nr') == 'on'
    tv = response.GET.get('tv') == 'on'
    num_movies = good_num(response.GET.get('movies'))
    if g or pg or pg13 or r or nr or tv:
        list = MovieList.objects.all()[0]
        movie_list = []
        if g:
            movies = list.movie_set.filter(rating='G').order_by('title')
            for movie in movies:
                movie_list.append([movie.title, movie.rating])
        if pg:
            movies = list.movie_set.filter(rating='PG').order_by('title')
            for movie in movies:
                movie_list.append([movie.title, movie.rating])
        if pg13:
            movies = list.movie_set.filter(rating='PG-13').order_by('title')
            for movie in movies:
                movie_list.append([movie.title, movie.rating])
        if r:
            movies = list.movie_set.filter(rating='R').order_by('title')
            for movie in movies:
                movie_list.append([movie.title, movie.rating])
        if nr:
            movies = list.movie_set.filter(rating='NR').order_by('title')
            for movie in movies:
                movie_list.append([movie.title, movie.rating])
        if tv:
            movies = list.movie_set.filter(rating='TV').order_by('title')
            for movie in movies:
                movie_list.append([movie.title, movie.rating])
        if len(movie_list) < num_movies:
            num_movies = 1
        generated = sample(movie_list,num_movies)
        ctx = {'generated':generated}
        return render(response, 'moviesdb/randomRes.html', ctx)
    return HttpResponseRedirect('/generator/')