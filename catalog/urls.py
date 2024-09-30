from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    ProductListView,
    ProductDetailView,
    contacts,
    ProductDeleteView,
    ProductCreateView,
    ProductUpdateView
)

app_name = CatalogConfig.name
urlpatterns = [
    path("", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),

    path('contacts/', contacts, name='contacts'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


