
from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from TodoItems import urls
from TodoItems import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('TodoItems.urls'))
]
