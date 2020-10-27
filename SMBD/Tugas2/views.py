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
  #yg ini buat atur halaman
  judul = "Product Supply"
  #yg ini buat judul kolom
  kolom = ["nama","total supply"]
  #kita ambil semua data produknya
  product_stacks=produk.objects.all()
  #kita buat sesuatu buat nampung data joinnya
  data = list()
  #kita rekonstruksi datanya
  for product in product_stacks:
    #kita ambil nama prioduknya dan agregasi agar keluar jumlah total produknya
    temp = mengemas.objects.filter(kode=product.kode).aggregate(Sum("jumlah"))['jumlah__sum']
    #karena mereka hanya suport dictionary buat output jadi saya bikin juga
    data.append({'nama':product.nama,'jumlah':temp})
  #terus kita masukin data yg didapet tadi ke kontextnya, kenapa nama nya serialize_data karena dat buakan dalam wujud object namun dict
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

