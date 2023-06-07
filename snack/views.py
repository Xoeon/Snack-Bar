from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Snack
from .forms import RequestForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='user:login')
def request_modify(request, snack_id):
    snack = get_object_or_404(Snack, pk=snack_id)
    if request.user != snack.requester:
        messages.error(request, '수정권한이 없습니다')
        return redirect('snack:detail', snack_id=snack.id)
    if request.user != snack.requester:
        messages.error(request, '수정권한이 없습니다')
        return redirect('snack:detail', snack_id=snack.id)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=snack)
        if form.is_valid():
            snack = form.save(commit=False)
            snack.save()
            return redirect('snack:detail', snack_id=snack.id)
    else:
        form = RequestForm(instance=snack)
    context = {'form': form}
    return render(request, 'snack/request_form.html', context)


@login_required(login_url='user:login')
def request_delete(request, snack_id):
    snack = get_object_or_404(Snack, pk=snack_id)
    if request.user != snack.requester:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('snack:detail', snack_id=snack.id)
    snack.delete()
    return redirect('snack:index')