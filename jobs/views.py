from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.utils.translation import gettext as _

def home(request):

    # from django.utils import translation
    # user_language = 'zh-cn'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] = user_language

    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #    del request.session[translation.LANGUAGE_SESSION_KEY]

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

    return render(request, 'jobs/home.html', {'jobs':jobs,})
