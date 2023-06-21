from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import F

from ..models import Snack


def index(request):
    page = request.GET.get('page', '1')
    
    # 상위 3개의 간식을 추천이 높은 순서로 가져옴
    top_snacks = Snack.objects.filter(vote_count__gt=0).order_by('-vote_count', 'create_date')[:3]
    
    # 나머지 간식들을 생성일자로 정렬하여 가져옴
    snack_request_list = Snack.objects.exclude(pk__in=top_snacks).order_by('-create_date')
    
    # 상위 3개의 간식을 추천이 높은 순서로 정렬
    top_snacks = sorted(top_snacks, key=lambda x: x.vote_count, reverse=True)
    
    # 상위 3개와 정렬된 나머지 간식들 합치기
    snacks = list(top_snacks) + list(snack_request_list)
    
    paginator = Paginator(snacks, 10)
    page_obj = paginator.get_page(page)
    
    context = {
        'top_snacks': top_snacks,
        'snack_request_list': page_obj
    }
    return render(request, 'snack/snack_request_list.html', context)
