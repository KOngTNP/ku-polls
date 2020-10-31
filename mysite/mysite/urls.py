from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('', include('polls.urls', namespace='loginpage')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),  

]