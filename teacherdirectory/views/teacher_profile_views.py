from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from teacherdirectory.forms import CSVImportForm
from techtest.settings import MEDIA_ROOT

import os.path
import csv, io

from teacherdirectory.models import TeacherProfile
from teacherdirectory.filters import TeacherProfileFilter
from teacherdirectory.constants import MAX_SUBJECTS, SUBJECTS_INDEX

class TeacherProfileDetailView(generic.DetailView):
    model = TeacherProfile

class TeacherProfileListView(generic.ListView):
    model = TeacherProfile

def teacher_profile_list_view(request):
    f = TeacherProfileFilter(request.GET, queryset=TeacherProfile.objects.all())
    return render(request, 'teacherdirectory/teacher_profile_list.html', {'filter': f})

class TeacherProfileDeleteView(DeleteView):
    model = TeacherProfile
    success_url = reverse_lazy('teacher_profiles')

def csv_teacher_profile_upload(request):
    """View for handling bulk importation of teacher profiles via csv"""
    template = "teacherdirectory/import_teacher_profiles.html"

    if request.method == "GET":
        return render(request, template, )

    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string)

    for row in csv.reader(io_string, quotechar="|"):
        if row[0] == '' or row[1] == '':
            continue
        
        # Check if this row's email address already exists in db, if it does, 
        # then don't save this teacher profile and skip to the next.
        tp_qs = TeacherProfile.objects.filter(email_address=row[3])
        if tp_qs.count() > 0:
            continue
        
        subjects = handle_subjects(row)
        
        pic = handle_teacher_profile_pictures(row[2])
        
        _, created = TeacherProfile.objects.update_or_create(
            first_name=row[0],
            last_name=row[1],
            profile_picture=pic,
            email_address=row[3],
            phone_number=row[4],
            room_number=row[5],
            subjects=subjects,
        )
    return render(request, template, context={})

def handle_teacher_profile_pictures(f):
    """Returns the parsed image file name if it is a jpg or png, otherwise returns a placeholder image."""
    l = len(f)
    ext = f[l - 4 : l].lower()
    if (ext == ".jpg" or ext == ".png") and os.path.exists(MEDIA_ROOT + "/" + f):
        return f
    return "placeholder.jpg" 

def handle_subjects(row):
    """Parses the subjects contained in the subjects column in the imported csv, and ensures that only the first 5 are returned, returns empty if none are found."""
    subjects = ""
    # if there is one subject only.
    l = len(row)
    m = l if l < (SUBJECTS_INDEX + MAX_SUBJECTS) else SUBJECTS_INDEX + MAX_SUBJECTS
    if l == SUBJECTS_INDEX + 1:
        subjects += row[SUBJECTS_INDEX]
    else:
        for i in range(SUBJECTS_INDEX, m):
            subjects += row[i]
            if i < m - 1:
                subjects += ", "
    subjects = subjects.replace("\"", "")
    return subjects 
