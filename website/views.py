from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic   import TemplateView
from website.models import Workout
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
import json
import datetime
from datetime import timedelta
from django.utils import timezone

#-------------------------------------------------------------------------------
# Page Views
#-------------------------------------------------------------------------------
class HomePageView(TemplateView):
    template_name = 'website/homepage.html'
    def get_context_data(self, **kwargs):
        user = self.request.user
        workouts = Workout.objects.filter(date=datetime.date.today())
        context = super(HomePageView,self).get_context_data(**kwargs)
        context = {
            'user': user,
            'workouts': workouts,
        }
        return context
