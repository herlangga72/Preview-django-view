from django.db import models
from datetime import date
# Create your models here.

class karyawan(models.Model):
	nomer			= models.IntegerField(primary_key=True)
	nama			= models.CharField(max_length=50)
	alamat		= models.CharField(max_length=50)
	tgl_masuk	= models.DateField(default=date.today)
	def __str__(self):
			return str(self.nama)

class produk(models.Model):
	kode							= models.CharField(max_length=50,primary_key=True)
	nama							= models.CharField(max_length=50)
	honor_pengemasan	= models.IntegerField()
	def __str__(self):
			return str(self.nama)

class mengemas(models.Model):
	kode		= models.ForeignKey(produk, on_delete=models.CASCADE)
	nomor		= models.ForeignKey(karyawan, on_delete=models.CASCADE)
	jumlah	= models.IntegerField()
	bonus		= models.IntegerField()
	tgl_kemas= models.DateField(default=date.today)
	def __str__(self):
			return str(self.kode)

