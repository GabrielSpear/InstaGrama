from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.timelines, name='allTimelines'),
    url(r'^accounts/profile/$', views.profile, name='myProfile'),
    url(r'^new/status/(?P<username>[-_\w.]+)$',
        views.new_status, name='newStatus'),
    url(r'^user/(\d+)', views.user_profile, name='userProfiles'),
