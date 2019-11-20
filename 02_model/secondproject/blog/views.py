from django.shortcuts import render
from .models import Blog

def home(request):
    blog = Blog.objects
    #모델로 부터 객체를 전달받을 수 있게 됩니다. 
    #이것을 쿼리셋이라 한다. : 쿼리셋 : 모델로부터 전달받은 객체목록 
    #이렇게 기능들을 표시하는 방법을 메소드라한다. 

    return render(request, 'home.html', {'blogs' : blog})
