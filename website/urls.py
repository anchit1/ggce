from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
  path('', views.home_page, name='home'),

  path('management/chief-patrons', views.mgmt_chief_patrons, name='chief_patrons'),
  path('management/secretary', views.mgmt_secretary, name='secretary'),
  path('management/executive-director', views.mgmt_exec_director, name='exec_director'),
  path('management/members-management', views.mgmt_members, name='members_mgmt'),
  path('management/group-director', views.mgmt_grp_director, name='grp_director'),

    path('courses/bsc', views.course_bsc, name='bsc'),
    path('courses/bsc/pcm', views.course_bsc_pcm, name='bsc_pcm'),
    path('courses/bsc/comp-applications', views.course_bsc_ca, name='bsc_ca'),

    path('courses/bcom', views.course_bcom, name='bcom'),

    path('courses/bba', views.course_bba, name='bba'),

  path('about/', RedirectView.as_view(pattern_name='home', permanent=False), name='about'),
  path('department/cse/about', views.cse_dept_about, name='cse_about')
]