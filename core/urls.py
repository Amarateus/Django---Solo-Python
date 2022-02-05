from django.contrib import admin
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomeView.as_view(), name='home'),   # El name o namespace sera relevante cuando queramos llamar las urls desde los templates

    path('blog/', include('blog.urls', namespace='blog')) # Incluyo del folder 'blog' el archivo 'urls.py'
]
