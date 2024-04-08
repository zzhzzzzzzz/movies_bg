from django.urls import path
from .views import *
urlpatterns = [
    path("week", MovieView1.as_view()),
    path("week/<int:id>", getweekmovie),

    path("box_office",MovieView2.as_view()),
    path('box_office/<int:id>', getboxoffice),

    path("hot", MovieView3.as_view()),
    path('hot/<int:id>', gethotmovie),

    path("top", MovieView5.as_view()),
    path('top/<int:id>', gettopmovie),

    path("search/<info>", MovieView4.as_view()),
    path('search/info/<int:id>',searchmovie),

    path('pie_data', login_required(['get'])(pie_data)),
    path('bar_data', login_required(['get'])(bar_data)),
    path('hist_data', login_required(['get'])(hist_data)),
    path('line_data', login_required(['get'])(line_data)),

    path("all_movies", login_required(['get'])(MovieView9.as_view())),

    path("year_label1", login_required(['get'])(MovieView6.as_view())),
    path("year_label2", login_required(['get'])(MovieView7.as_view())),
    path("year_label3", login_required(['get'])(MovieView8.as_view())),

    path("kind_label1", login_required(['get'])(MovieView10.as_view())),
    path("kind_label2", login_required(['get'])(MovieView11.as_view())),
    path("kind_label3", login_required(['get'])(MovieView12.as_view())),
    path("kind_label4", login_required(['get'])(MovieView13.as_view())),
    path("kind_label5", login_required(['get'])(MovieView14.as_view())),
    path("kind_label6", login_required(['get'])(MovieView15.as_view())),
    path("kind_label7", login_required(['get'])(MovieView16.as_view())),
    path("kind_label8", login_required(['get'])(MovieView17.as_view())),


]