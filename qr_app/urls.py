from django.urls import path
from .views import login, dashboard, logout, set_ip, scan_page, check_in, check_out

urlpatterns = [
    path('', login, name="login"),
    path('dashboard/', dashboard, name="dash"),
    path('logout/', logout, name="logout"),
    path('set_ip/', set_ip, name="set_ip"),
    path('scan_page/<slug:id>/', scan_page, name="scan_page"),
    path('check_in/<slug:id>/', check_in, name="check_in"),
    path('check_out/<slug:id>/', check_out, name="check_out"),
]