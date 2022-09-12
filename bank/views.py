from django.shortcuts import render

from .forms import TaskForm


def form_view(request):
    return render(request, 'test_form.html', {'form': TaskForm()})