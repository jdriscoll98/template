from django.conf.urls import url, include
from django.urls import path
from . import views
from website.views	import HomePageView
# Application Routes (URLs)

app_name = 'website'

urlpatterns = [
    	# General Page Views
		url(r'^$',HomePageView.as_view(), name='homepage_view'),
		]
