from django.shortcuts import render
from django.utils import timezone
from .models import Snack
from .forms import SnackForm


def index(request):
    snack_request_list = Snack.objects.order_by('-create_date')
    context = {'snack_request_list': snack_request_list}
    return render(request, 'snack/snack_request_list.html', context)


def snack_request_create(request):
    form = SnackForm()
    return render(request, 'snack/snack_request_create.html', {'form': form})
