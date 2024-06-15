from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace="pages")),
    path('blogs/', include('blogs.urls', namespace="blogs")),
    path('products/', include('products.urls', namespace="products")),
    path('users/', include('users.urls', namespace="users")),
    path('orders/', include('orders.urls', namespace="orders"))

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)