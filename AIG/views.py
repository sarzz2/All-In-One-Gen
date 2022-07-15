import random

from django.shortcuts import render
from .gen_files import quotes, rand_images, music, createMaze, passwordGen, color, datetimeGen


def home(request):
    quote_query = quotes.formatted_quote()
    return render(request, "home.html", {"data": quote_query})


def about(request):
    return render(request, "about.html")


def image_gen(request):
    rand_images.random_images()
    return render(request, "image_gen.html")


def music_gen(request):
    music.music_gen(random.randint(1, 10))
    return render(request, 'music_gen.html')


def maze_gen(request):
    createMaze.run(20, 20)
    return render(request, 'maze_gen.html')


def password_gen(request):
    if request.method == "POST":
        x = request.POST.get("length", None)
        ans = passwordGen.passw(int(x))
        return render(request, 'password.html', {"data": ans})
    return render(request, 'password.html')


def color_gen(request):
    x = color.hex()
    y = color.rgb()
    return render(request, 'color.html', {"hex": x, "rgb": y})


def datetime_gen(request):
    date_and_time = datetimeGen.gen_datetime().strftime("%m/%d/%Y, %H:%M:%S")
    return render(request, 'datetime_gen.html', {"data": date_and_time})
