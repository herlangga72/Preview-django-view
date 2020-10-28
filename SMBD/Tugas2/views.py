from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime
from .models import *
# Create your views here.

def karyawan_all(request):
  judul = "Karyawan Order By Time"
  kolom = ["nomer","nama","alamat","tanggal masuk"]
  fetched_data = karyawan.objects.order_by("tgl_masuk")
  context = dict(serialized_data=fetched_data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)

def product_counter(request):
  judul = "Product Supply"
  kolom = ["nama","total supply"]
  data = mengemas.objects.values("kode__nama").annotate(jumlah=Sum("jumlah"))
  context = dict(serialized_data=data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)

def karyawan_works_on(request):
  judul = "Barang yang dibungkus Hari ini"
  kolom = ["nama","list barang"]
  workers=karyawan.objects.all()
  data = list()
  for worker in workers:
    temp = mengemas.objects.filter(tgl_kemas=datetime.now().date()).filter(nomor=worker.nomer)
    data.append({'nama':worker.nama,'type':temp})
  context = dict(serialized_data=data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)


def Bonus_bulanan(request):
  judul = "Bonus Karyawan bulan ini"
  kolom = ["nama","bonus"]
  data=mengemas.objects.values('nomor__nama').filter(tgl_kemas__month=datetime.now().month).annotate(jumlah=Sum("bonus"))
  context = dict(serialized_data=data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)

def testing(request):
  judul = "Bonus Karyawan bulan ini"
  kolom = ["nama","bonus"]
  #ambil data mengemas dan juga filter berdasar bulan ini
  workers=karyawan.objects.all()
  data = list()
  #reconstuct data
  for worker in workers:
    bonus_one_month= mengemas.objects.filter(tgl_kemas__month=datetime.now().month).filter(nomor=worker.nomer).aggregate(Sum("bonus"))['bonus__sum']
    data.append({'nama':worker.nama, 'jumlah':bonus_one_month})
  context = dict(serialized_data=data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)