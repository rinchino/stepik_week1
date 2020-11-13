from django.shortcuts import render

# Create your views here.
from django.views import View
from django.http import HttpResponse, Http404, HttpResponseNotFound


class FirstView(View):

    def get(self, request):
        return HttpResponse('first')


class SecondView(View):

    def get(self, request):
        return HttpResponse('second')


class ThirdView(View):

    def get(self, request):
        return HttpResponse('third')


class DepartureView(View):

    def get(self, request):
        return render(request,'departure.html')


class TourView(View):

    def get(self, request):
        weeks = 15
        course = "Flask"
        group = "A 0101"

        context = {
           "weeks": weeks,
            "course": course,
            "group": group,
        }
        return render(request,'tour.html', context=context)


class StudentView(View):

    def get(self, request, student_id):
        students = {
            1: "Смирнов Хольгер Филиппович",
            2: "Демидович Налина Кирилловна",
            3: "Рыбакова Хитер Валерьвна",
            4: "Жуков Орион Святославович"
        }
        if student_id not in students:
            return HttpResponseNotFound('Такой студент не найден')

        context = {
            'student': students[student_id]
        }
        return render(request,'student.html', context=context)