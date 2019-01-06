from django.conf.urls import url, include
from django.urls import path
from .views import shifts_available_page_view
from . import views
# Application Routes (URLs)

app_name = 'website'

urlpatterns = [
    	# General Page Views
		url(r'^$', views.homepage_view, name='homepage_view'),
		url(r'^post-shift/(?P<pk>\d+)$', views.PostShiftView.as_view(), name='post_shift'),
		url(r'^shifts-available$', views.shifts_available_page_view, name='ShiftsAvailableView'),
		url(r'^pick-up-shift/(?P<pk>\d+)$', views.pick_up_shift_view, name='pick_up_shift'),
]
