from django.urls import path
from teacherdirectory.views import *

urlpatterns = [
    #path('teacher_profiles/', TeacherProfileListView.as_view(), name='teacher_profiles'),
    path('teacher_profiles/', teacher_profile_list_view, name='teacher_profiles'),
    path('teacher_profile/<int:pk>', TeacherProfileDetailView.as_view(), name='teacher_profile_detail'),
    path('teacher_profile/delete/<int:pk>', TeacherProfileDeleteView.as_view(), name='teacher_profile_delete'),
    path('teacher_profiles/import//', csv_teacher_profile_upload, name="import_teacher_profiles"),
] 
