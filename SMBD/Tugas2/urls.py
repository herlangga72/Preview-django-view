from .views import *
from django.urls import path, include
urlpatterns = [
    path('karyawan', karyawan_all),
    path('Product_stocks', product_counter),
    path('Bonus_In_This_Month', Bonus_bulanan),
    path('gt_krywn_prf_mth', karyawan_works_on),
    path('gt_krywn_prf_hr', karyawan_works_on)
]