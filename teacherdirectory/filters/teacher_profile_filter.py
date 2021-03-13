import django_filters
from teacherdirectory.models import TeacherProfile

class TeacherProfileFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='startswith')
    subjects = django_filters.CharFilter(lookup_expr='contains')
    class Meta:
        model = TeacherProfile
        fields = ["last_name", "subjects", ]