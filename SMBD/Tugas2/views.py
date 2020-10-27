from django.shortcuts import render
from django.db.models import Sum
# Create your views here.
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
  product_stacks=produk.objects.all()
  data = list()
  #reconstuct data
  for product in product_stacks:
    a = mengemas.objects.filter(kode=product.kode)
    a= a.aggregate(Sum("jumlah"))['jumlah__sum']
    data.append({'nama':product.nama,'jumlah':a})
  context = dict(serialized_data=data,title=judul,column_name=kolom)
  return render(request, 'index.html', context)
