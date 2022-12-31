from django.urls import path
from jobs import views
urlpatterns = [
    path('work-now',views.workNow),
    path('work-end',views.workEnd),
    path('jobs',views.allJobs),
    path('<int:id>',views.visit),
]