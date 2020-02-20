from django.shortcuts import render

posts = [
    {
        'author': 'deathyard',
        'title' : 'ABC',
        'content':'first post',
        'date':'2/1/20'
    },
    {
        'author': 'scream',
        'title' : 'XYZ',
        'content':'second post',
        'date':'3/1/20'
    },
]

def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html', {'title' : 'About'})
