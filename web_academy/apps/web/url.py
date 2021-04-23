from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('about/', About.as_view(), name="about"),
    path('trainer/', Trainers.as_view(), name="trainer"),
    path('lesson/', Lessons.as_view(), name="lesson"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('test_request/', TestRequestView.as_view(), name="test_request"),
    path('offer/', OffersView.as_view(), name="offer"),
    path('lesson/<slug:slug>/', DetailLessonForm.as_view(), name='detail_lesson'),

]
