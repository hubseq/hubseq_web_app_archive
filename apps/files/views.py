from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# django-storages
from django.core.files.storage import default_storage
from os import path

# Create your views here.
@login_required
def my_files(request):
    dirs = default_storage.listdir('test')
    return render(request, 'files/my_files.html', context={
        'active_tab': 'my_files',
        'dirs': list(dirs),
    })

@login_required
def my_files_subdir(request, subdir):
    subdir_list = subdir.split('_-_')
    subdir_path = ''
    for s in subdir_list:
        subdir_path += s + '/'
    dirs = default_storage.listdir(path.join('test',subdir_path))
    return render(request, 'files/my_files_sub.html', context={
        'active_tab': 'my_files',
        'dirs': list(dirs),
        'subdir': str(subdir),
        'subdir_path': str(subdir_path),
    })
