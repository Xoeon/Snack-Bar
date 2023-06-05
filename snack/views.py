from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Snack
from .forms import RequestForm


def index(request):
    snack_request_list = Snack.objects.order_by('-create_date')
    context = {'snack_request_list': snack_request_list}
    return render(request, 'snack/snack_request_list.html', context)


def request_create(request):
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            snack = form.save(commit=False)
            snack.create_date = timezone.now()
            snack.save()
            return redirect('snack:index')
    else:
        form = RequestForm()
    context = {'form': form}
    return render(request, 'snack/request_form.html', context)
