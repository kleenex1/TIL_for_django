from django.shortcuts import render
import random

# Create your views here.


def index(request):

    return render(request, "index.html")


def print_text(request):
    past = ["말", "돼지", "고양이", "강아지", "사자", "호랑이"]
    choice = random.choice(past)
    text = request.GET.get("_text")
    context = {
        "text": text,
        "choice": choice,
    }

    return render(request, "text.html", context)


def is_odd_even(request, number):
    context = dict()
    context["number"] = number
    if number == 0:
        context["num"] = 0
    elif number % 2 == 0:
        context["num"] = "짝수"
    elif number % 2 == 1:
        context["num"] = "홀수"
    return render(request, "is-odd-even.html", context)


def calculate(request, num1, num2):
    context = dict()
    context["num1"] = num1
    context["num2"] = num2
    context["plus"] = num1 + num2
    context["minus"] = num1 - num2
    context["divide"] = num1 // num2
    context["multi"] = num1 * num2
    return render(request, "calculate.html", context)


def lorem(request):
    return render(request, "lorem.html")


def lorem_page(request):
    foods = ["바나나", "사과", "짜장면", "삼겹살", "떡볶이"]
    para = request.GET.get("para")
    word = request.GET.get("word")
    rand_list = []
    for _ in range(int(word)):
        rand = random.choice(foods)
        rand_list.append(rand)
    result = [1] * int(para)
    context = {
        "rand_list": rand_list,
        "result_list": result,
    }
    return render(request, "lorem-page.html", context)
