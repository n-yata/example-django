from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy

from .models import Diary

class DiaryList(ListView):
    model = Diary
    context_object_name = "diarys"
    ordering = "-day"

class DiaryDetail(DetailView):
    model = Diary
    context_object_name = "diary"

class DiaryCreate(CreateView):
    model = Diary
    fields ="__all__"
    success_url = reverse_lazy("diary_list")

class DiaryUpdate(UpdateView):
    model = Diary
    fields ="__all__"
    success_url = reverse_lazy("diary_list")

class DiaryDelete(DeleteView):
    model = Diary
    context_object_name = "diary"
    success_url = reverse_lazy("diary_list")