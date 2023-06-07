from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import RequestForm
from ..models import Snack


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
        return redirect('snack:index')
    if request.user != snack.requester:
        messages.error(request, '수정권한이 없습니다')
        return redirect('snack:index')
    if request.method == "POST":
        form = RequestForm(request.POST, instance=snack)
        if form.is_valid():
            snack = form.save(commit=False)
            snack.save()
            return redirect('snack:index')
    else:
        form = RequestForm(instance=snack)
    context = {'form': form}
    return render(request, 'snack/request_form.html', context)


@login_required(login_url='user:login')
def request_delete(request, snack_id):
    snack = get_object_or_404(Snack, pk=snack_id)
    if request.user != snack.requester:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('snack:index')
    snack.delete()
    return redirect('snack:index')