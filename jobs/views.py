from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def home(request):
    jobs_list = Job.objects.all()
    paginator = Paginator(jobs_list,9)

    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        jobs = paginator.page(page)
    except(EmptyPage, InvalidPage):
        jobs = paginator.page(paginator.num_pages)

    return render(request, 'jobs/home.html', {'jobs':jobs})
