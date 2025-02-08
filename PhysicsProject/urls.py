from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('energy/', include('energy_calculator.urls')),
    path('', RedirectView.as_view(url='/energy/')),
]
