from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request): # 요청을 받으면 index.html을 보여줄 수 있게 이렇게 응답
    return render(request, 'Landing/index.html') # Landing 폴더에 있는 index.html을 뱉어라.
    # return HttpResponse('Hello')

def study(req):
    return render(req, 'Landing/study.html')