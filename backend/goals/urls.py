from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('goals', views.GoalView)
router.register('tasks', views.TaskView)


urlpatterns = [
    path('', include(router.urls)),
]