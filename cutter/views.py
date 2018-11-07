from django.shortcuts import render

# Create your views here.
def question_list(request):
    return render(request, 'cutter/question_list.html',{})