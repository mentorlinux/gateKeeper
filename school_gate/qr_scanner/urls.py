from django.urls import path
from . import views


urlpatterns = [
    path('', views.scan_qr_code, name='scan_qr_code'),
    path('get-scanned-qr-codes/', views.get_scanned_qr_codes, name='get_scanned_qr_codes'),  # AJAX endpoint
]