from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Allcourses
from django.template import loader

def Courses(request):
    ac=Allcourses.objects.all()
    template=loader.get_template('TechnicalCourses/Courses.html')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request, couse_id):
    course=get_object_or_404(Allcourses, pk=couse_id)
    return render(request, 'TechnicalCourses/detail.html',{'course':course})

def yourchoice(request, course_id):
    course=get_object_or_404(Allcourses, pk=course_id)
    try:
        selected_ct=course.details_set.get(pk=request.POST['choice'])
    except (KeyError, Allcourses.DoesNotExist):
        return render(request, 'TechnicalCourses/detail.html',{
            'course':course,
            'error_message':"Select a valid option",
        })
    else:
        selected_ct.your_choice=True
        selected_ct.save()
        return render(request, 'TechnicalCourses/detail.html', {'course':course})
