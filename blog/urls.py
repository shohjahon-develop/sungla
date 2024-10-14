from django.urls import path
from .views import (index, contact, about, shop, glasses, aboutsdetailview, glassdetailview, bestsdetailview,
                    aboutssdetailview, SearchResultsList)





urlpatterns = [
path('', index, name='index'),
    path('shop/',shop , name='shop'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('glasses/', glasses, name='glasses'),
    path('abouts/<slug:abouts>', aboutsdetailview, name='aboutsDetail'),
    path('glass/<slug:glass>', glassdetailview, name='glassDetail'),
    path('bests/<slug:bests>', bestsdetailview, name='bestsDetail'),
    path('aboutss/<slug:aboutss>',aboutssdetailview, name='aboutssDetail'),
    path('search/', SearchResultsList.as_view(), name='search_result')
    ]