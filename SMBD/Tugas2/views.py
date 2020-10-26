from django.shortcuts import render
from .models import *
# Create your views here.

def karyawan_all(request):
  judul = "karyawan"
  kolom = ["nomer","nama","alamat","tanggal masuk"]
  fetched_data = karyawan.objects.orderby()
  context = dict(serialized_data=fetched_data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)

def   