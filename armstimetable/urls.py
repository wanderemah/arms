from . import views
from django.conf.urls import url

app_name = 'timetable'

urlpatterns = [
    url(r'^tutors/activities/', views.docket1, name='docket'),
    url(r'^student/activities/', views.docket2, name='docket2'),
    url(r'^signup/', views.Sign_up.as_view(), name='signup'),
    url(r'^add_activity/', views.Action.as_view(), name='addactivity'),
    url(r'^staff/tutor/(?P<tutor>\D+)$', views.tutor_detail, name='tutordetails'),
    url(r'^student/tutor/(?P<tutor>\D+)$', views.tutor_detail2, name='tutordetails2'),
    # url(r'^student/(?P<student>\D+)$', views.student_detail, name='studentdetails'),
    url(r'^query/', views.Question.as_view(), name='query'),
    url(r'^response/', views.Respond.as_view(), name='repond'),
    url(r'^staff/topic/(?P<topic>\D+)$', views.topic_detail, name='topicdetails'),
    url(r'^student/topic/(?P<topic>\D+)$', views.topic_detail2, name='topicdetails2'),
    url(r'^edit_activity/(?P<pk>\D+)$', views.Update.as_view(), name='editactivity'),
    url(r'^delete_activity/(?P<pk>\D+)$', views.delete, name='deleteactivity'),
    url(r'^delete_qquery/(?P<pk>\D+)$', views.deletequery, name='deletequery'),
    # url(r'^description',views.description, name='description'),
]
