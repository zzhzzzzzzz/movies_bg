from django.urls import path
from .views import *
urlpatterns = [
    path("week", login_required(['get'])(MovieView1.as_view())),
    path("week/<int:id>", getweekmovie),

    path("box_office", login_required(['get'])(MovieView2.as_view())),
    path('box_office/<int:id>', getboxoffice),

    path("hot", login_required(['get'])(MovieView3.as_view())),
    path('hot/<int:id>', gethotmovie),

    path("top", login_required(['get'])(MovieView5.as_view())),
    path('top/<int:id>', gettopmovie),

    path("search/<info>", login_required(['get'])(MovieView4.as_view())),
    path('search/info/<int:id>',searchmovie),

    path('pie_data', pie_data),
    path('bar_data', bar_data),
    path('hist_data', hist_data),
    path('line_data', line_data),
]