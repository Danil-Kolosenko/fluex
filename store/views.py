from django.shortcuts import render

def store(request):
    content = []
    return render(request, 'store/store.html', content)
