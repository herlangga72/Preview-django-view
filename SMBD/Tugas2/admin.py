from django.contrib import admin
from .models import produk, mengemas, karyawan
# Register your models here.
@admin.register(karyawan)
class karyawanAdmin(admin.ModelAdmin):
	list_display =('nomer','nama','alamat','tgl_masuk')
    
@admin.register(produk)
class produkAdmin(admin.ModelAdmin):
  list_display=("kode","nama", "honor_pengemasan")
@admin.register(mengemas)
class mengemasAdmin(admin.ModelAdmin):
  list_display=("kode","nomor","jumlah","bonus","tgl_kemas" )



