from django.shortcuts import render
from datetime import datetime
from django.http import Http404

# Create your views here.
def index(request):
    today = datetime.today().date()
    context = {"date": today}

    return render(request, 'foods/index.html', context=context)

def food_detail(request, food):
    context = dict()
    if food == "chicken":
        context["name"] = "양념치킨"
        context["description"] = "처갓집 양념치킨 !!"
        context["price"] = 20000
        context["img_path"] = "foods/images/chicken.jpg"
    else :
        raise Http404("잘못된 경로입니다!")
    return render(request, 'foods/detail.html', context)