from django.urls import path
from . import views

urlpatterns = [
    # Category endpoints
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:id>/', views.CategoryDetailView.as_view(), name='category-detail'),

    # Product endpoints
    path('', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('<int:product_id>/images/', views.ProductImageUploadView.as_view(), name='product-image-upload'),

    # Review endpoints
    path('<int:product_id>/reviews/', views.ProductReviewView.as_view(), name='product-reviews'),

    # Wishlist endpoints
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('wishlist/<int:id>/', views.WishlistDetailView.as_view(), name='wishlist-detail'),

    # Admin endpoints
    path('admin/stats/', views.AdminProductStatsView.as_view(), name='admin-product-stats'),
    path('admin/low-stock/', views.AdminLowStockView.as_view(), name='admin-low-stock'),
]