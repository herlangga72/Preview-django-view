from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime
from .models import *

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
  judul = "testing"
  kolom = ["nama","item","jumlah"]
  data = mengemas.objects.values("nomor__nama","kode__nama").filter(tgl_kemas__month=datetime.now().month).annotate(hasil=Sum("jumlah")).order_by("nomor__nama")
  context = dict(serialized_data=data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)

#daftar nama karyawan, nama produk dan jumlah produk yang dikemas di bulan ini