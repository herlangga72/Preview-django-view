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
  product_stacks=produk.objects.all()
  data = list()
  #reconstuct data
  for product in product_stacks:
    temp = mengemas.objects.filter(kode=product.kode).aggregate(Sum("jumlah"))['jumlah__sum']
    data.append({'nama':product.nama,'jumlah':temp})
  context = dict(serialized_data=data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)

def karyawan_works_on(request):
  judul = "Barang yang dibungkus Hari ini"
  kolom = ["nama","list barang"]
  workers=karyawan.objects.all()
  data = list()
  #reconstuct data
  for worker in workers:
    temp = mengemas.objects.filter(tgl_kemas=datetime.now().date()).filter(nomor=worker.nomer)
    data.append({'nama':worker.nama,'type':temp})
  context = dict(serialized_data=data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)

def testing(request):
  return render(request, 'index.html')

