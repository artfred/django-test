from django.shortcuts import render

# Create your views here.
def app(request):
    layouts = ""
    context = {
        'layouts':layouts,
    }
    return render(request, 'app/index.html', context)
