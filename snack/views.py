from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Snack
from .forms import RequestForm
from django.core.paginator import Paginator


def index(request):
    page = request.GET.get('page', '1')
    snack_request_list = Snack.objects.order_by('-create_date')
    paginator = Paginator(snack_request_list, 10)
    page_obj = paginator.get_page(page)
    context = {'snack_request_list': page_obj}
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
