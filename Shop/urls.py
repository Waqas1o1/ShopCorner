from django.urls import path
from . import views
urlpatterns = [ 
                path('',views.Index,name='ShopHome'),
                path('about/',views.About,name='aboutpage'),
                path('contact/',views.Contact,name='contactPage'),
                path('tracker/',views.Tracker,name='trackerpage'),
                path('search/',views.Search,name='searchpage'),
                path('products/<int:pid>',views.Products,name='productviewpage'),
                path('checkout/',views.Checkout,name='checkoutpage')
              ]