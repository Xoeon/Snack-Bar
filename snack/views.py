from django.shortcuts import render
from .models import Snack


def index(request):
    snack_request_list = Snack.objects.order_by('-create_date')
    context = {'snack_request_list': snack_request_list}
    return render(request, 'snack/snack_request_list.html', context)
