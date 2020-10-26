from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
  fetched_data = karyawan.objects.all()[::1]
  context = dict(serialized_data=fetched_data)
  return render(request, 'index.html', context)