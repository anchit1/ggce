from django.shortcuts import render


# Create your views here.
def home_page(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'website/home/home_page.html', context)


def cse_dept_about(request):
    return render(request, 'website/departments/cse/about.html')


def mgmt_chief_patrons(request):
    context = {
        'title': 'Management'
    }
    return render(request, 'website/management/chief_patrons.html', context)


def mgmt_secretary(request):
    context = {'title': 'Management'}
    return render(request, 'website/management/secretary.html', context)


def mgmt_exec_director(request):
    context = {'title': 'Management'}
    return render(request, 'website/management/exec_director.html', context)


def mgmt_members(request):
    context = {'title': 'Management'}
    return render(request, 'website/management/mgmt_members.html', context)


def mgmt_grp_director(request):
    context = {'title': 'Management'}
    return render(request, 'website/management/grp_director.html', context)


def course_bsc(request):
    context = {'title': 'Courses'}
    return render(request, 'website/courses/bsc.html', context)


def course_bsc_pcm(request):
    context = {'title': 'Courses'}
    return render(request, 'website/courses/bsc_pcm.html', context)


def course_bsc_ca(request):
    context = {'title': 'Courses'}
    return render(request, 'website/courses/bsc_ca.html', context)


def course_bcom(request):
    context = {'title': 'Courses'}
    return render(request, 'website/courses/bcom.html', context)


def course_bba(request):
    context = {'title': 'Courses'}
    return render(request, 'website/courses/bba.html', context)

