from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^team/$', views.team, name='team'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^courses_detail/$', views.courses_detail, name='courses_detail'),
    url(r'^login_web/$', views.login_web, name='login_web'),

]
