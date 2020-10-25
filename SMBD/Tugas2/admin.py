from django.contrib import admin
from .models import produk, mengemas, karyawan
# Register your models here.
admin.site.register(mengemas)
admin.site.register(produk)
admin.site.register(karyawan)

