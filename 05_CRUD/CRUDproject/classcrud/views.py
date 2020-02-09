from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy #리다이렉트 시켜주기
from django.views.generic.list import ListView #데이터 보여주기 
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #데이터 추가 
from .models import ClassBlog

class BlogView(ListView):   #html 템플릿 : 블로그 리스트를 담은 html -> (소문자 모델)_list.html
    model = ClassBlog

class BlogCreate(CreateView): # html : form(입력공간)을 갖고있는 html -> (소문자 모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url =reverse_lazy('list')


class BlogDetail(DetailView):   # html : 상세페이지를 담은 html -> (소문자 모델)_detail.html
    model = ClassBlog

class BlogUpdate(UpdateView):    # html : form(입력공간)을 갖고있는 html -> (소문자 모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url =reverse_lazy('list')

class BlogDelete(DeleteView):       # html : 진짜 지울꺼야?  -> (소문자 모델)_confirm_delete.html
    model = ClassBlog
    success_url =reverse_lazy('list')

