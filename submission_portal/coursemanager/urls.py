from django.urls import path
from . import views

app_name = 'coursemanager'

urlpatterns = [
    path('', views.index, name = 'home'),
    path('submissions/<int:pk>/', views.SubmissionsView, name = 'submissions-view'),
    path('assignment/add/', views.AddAssignment, name = 'add-assignment'),
    path('assignment/<int:pk>/', views.EditAssignment, name = 'edit-assignment'),
    path('media/<path:file>', views.MediaView, name='media'),
    path('submit/<int:pk>/', views.SubmitAssignment, name = 'submit-assignment'),
    path('edit-submitted/<int:pk1>/<int:pk2>', views.EditSubmittedAssignment, name = 'edit-submitted-assignment'),
    path('evaluate/<int:pk1>/<int:pk2>', views.EvaluateAssignment, name = 'evaluate-assignment'),
]   