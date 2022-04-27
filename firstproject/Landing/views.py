from django.shortcuts import render
from django.core.files.storage import default_storage
from django.http import HttpResponse
from stickerUtils.sticker import stickerGen

# Create your views here.
def index(request): # 요청을 받으면 index.html을 보여줄 수 있게 이렇게 응답
    return render(request, 'Landing/index.html') # Landing 폴더에 있는 index.html을 뱉어라.
    # return HttpResponse('Hello')

def study(req):
    return render(req, 'Landing/study.html')

def sticker(req): # sticker.html을 볼 수 있게
    return render(req, 'Landing/sticker.html')

def stickerResult(req):
    if req.method == "POST": # 통신을 받았는데 만약 그 방식이 post라면
        try:
            imgMemory = req.FILES["image"] # 통신에서 image를 inmemory에 저장되어 있는 값으로 읽어 들임
            imgByte = imgMemory.read() # 통신에서 image를 Byte로 읽어 들임
            convertImg = "data:image/jpg;base64, " + str(stickerGen(imgByte)) # Html img 태그에서 출력할수 있도록 base64 타입으로 변환
            return render(req, 'Landing/stickerResult.html', {'image': convertImg})
        except:
            return HttpResponse("보여줄 이미지가 없습니다!") # image 파일이 없으면 처리
    else:
        return HttpResponse("보여줄 이미지가 없습니다!") # post 통신이 아니면(get 통신) 자료를 보낼수 없어서 예외 처리