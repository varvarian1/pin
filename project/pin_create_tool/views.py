from django.shortcuts import render, redirect

from .forms import PinForm

def index(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)  

        form = PinForm(request.POST, request.FILES)  

        if form.is_valid():
            form.save()
            return redirect('main:main')
        else:
            print(form.errors)
    else:
        form = PinForm()

    return render(request, 'main/index.html', {'form': form})

