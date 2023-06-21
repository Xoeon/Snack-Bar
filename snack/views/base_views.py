from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Snack


def index(request):
    page = request.GET.get('page', '1')
    top_snacks = Snack.objects.order_by('-vote_count')[:3]
    snack_request_list = Snack.objects.order_by('-create_date')
    paginator = Paginator(snack_request_list, 10)
    page_obj = paginator.get_page(page)
    context = {'snack_request_list': page_obj}
    return render(request, 'snack/snack_request_list.html', context)