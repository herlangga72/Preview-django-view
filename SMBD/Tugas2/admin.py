from django.contrib import admin
from .models import produk, mengemas, karyawan
# Register your models here.
@admin.register(karyawan)
class karyawanAdmin(admin.ModelAdmin):
  list_display =['nomer','nama','alamat','tgl_masuk']
  list_filter=('tgl_masuk',)
  search_fields=['nama']
    
@admin.register(produk)
class produkAdmin(admin.ModelAdmin):
  list_display=("kode","nama", "honor_pengemasan")
  search_fields=['nama']
  
@admin.register(mengemas)
class mengemasAdmin(admin.ModelAdmin):
  list_display=("kode","nomor","jumlah","bonus","tgl_kemas" )
  list_filter=('tgl_kemas',)
  search_fields=['nomer']



