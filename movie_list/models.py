from django.db import models

# class Movie(models.Model): #id 主键 title，postdate，author 表post
#     class Meta:
#         db_table='movie'
#     id=models.BigAutoField(primary_key=True)
#     title=models.CharField(max_length=128,null=False,unique=False)
#     releasedate=models.CharField(max_length=128,null=False,unique=False)
#     director=models.CharField(max_length=128,null=False,unique=False)
#
#     def __repr__(self):
#         return "<Movie:{} {} {}>".format(self.id,self.title,self.releasedate)
#
#     __str__=__repr__
#
# class Content(models.Model): #id 主键 外键，content 表content
#     class Meta:
#         db_table="content"
#     movie=models.OneToOneField(Movie,on_delete=models.PROTECT,primary_key=True)
#     rate =models.DecimalField(max_digits=2,decimal_places=1,null=True)
#     kind =models.CharField(max_length=128,null=False,unique=False)
#     country =models.CharField(max_length=128,null=False,unique=False)
#     language =models.CharField(max_length=128,null=False,unique=False)
#     time =models.CharField(max_length=128,null=False,unique=False)
#     actor =models.TextField(null=True)
#
#     def __repr__(self):
#         return "<Content:{} {}>".format(self.pk,self.actor)
#
#     __str__=__repr__

class WeekMovies(models.Model): #id 主键 外键，content 表content
    class Meta:
        db_table="week_movies"
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False, unique=False)
    releasedate = models.CharField(max_length=128, null=False, unique=False)
    director = models.CharField(max_length=128, null=False, unique=False)
    rate =models.DecimalField(max_digits=2,decimal_places=1,null=True)
    kind =models.CharField(max_length=128,null=False,unique=False)
    country =models.CharField(max_length=128,null=False,unique=False)
    language =models.CharField(max_length=128,null=False,unique=False)
    time =models.CharField(max_length=128,null=False,unique=False)
    actor =models.TextField(null=True)

    def __repr__(self):
        return "<WeekMovies:{} {}>".format(self.pk,self.actor)

    __str__=__repr__

class BoxOffice(models.Model): #id 主键 外键，content 表content
    class Meta:
        db_table="boxoffice"
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False, unique=False)
    releasedate = models.CharField(max_length=128, null=False, unique=False)
    director = models.CharField(max_length=128, null=False, unique=False)
    rate =models.DecimalField(max_digits=2,decimal_places=1,null=True)
    kind =models.CharField(max_length=128,null=False,unique=False)
    country =models.CharField(max_length=128,null=False,unique=False)
    language =models.CharField(max_length=128,null=False,unique=False)
    time =models.CharField(max_length=128,null=False,unique=False)
    actor =models.TextField(null=True)

    def __repr__(self):
        return "<BoxOffice:{} {}>".format(self.pk,self.actor)

    __str__=__repr__

class HotMovies(models.Model): #id 主键 外键，content 表content
    class Meta:
        db_table="hotmovies"
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False, unique=False)
    releasedate = models.CharField(max_length=128, null=False, unique=False)
    director = models.CharField(max_length=128, null=False, unique=False)
    rate =models.DecimalField(max_digits=2,decimal_places=1,null=True)
    kind =models.CharField(max_length=128,null=False,unique=False)
    country =models.CharField(max_length=128,null=False,unique=False)
    language =models.CharField(max_length=128,null=False,unique=False)
    time =models.CharField(max_length=128,null=False,unique=False)
    actor =models.TextField(null=True)

    def __repr__(self):
        return "<HotMovies:{} {}>".format(self.pk,self.actor)

    __str__=__repr__

class AllMovies(models.Model): #id 主键 外键，content 表content
    class Meta:
        db_table="allmovies"
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=128, null=False, unique=False)
    releasedate = models.CharField(max_length=128, null=False, unique=False)
    director = models.CharField(max_length=128, null=False, unique=False)
    rate =models.DecimalField(max_digits=2,decimal_places=1,null=True)
    kind =models.CharField(max_length=128,null=False,unique=False)
    country =models.CharField(max_length=128,null=False,unique=False)
    language =models.CharField(max_length=128,null=False,unique=False)
    time =models.CharField(max_length=128,null=False,unique=False)
    actor =models.TextField(null=True)

    def __repr__(self):
        return "<AllMovies:{} {}>".format(self.pk,self.actor)

    __str__=__repr__

class TopMovies(models.Model):
    class Meta:
        db_table="topmovies"
    id = models.BigAutoField(primary_key=True)
    C_title = models.CharField(max_length=128, null=False, unique=False)
    E_title = models.CharField(max_length=128, null=False, unique=False)
    releasedate = models.CharField(max_length=128, null=False, unique=False)
    director = models.CharField(max_length=128, null=False, unique=False)
    rate =models.DecimalField(max_digits=2,decimal_places=1,null=True)
    kind =models.CharField(max_length=128,null=False,unique=False)
    country =models.CharField(max_length=128,null=False,unique=False)
    url =models.CharField(max_length=128,null=False,unique=False)
    people=models.CharField(max_length=128, null=False, unique=False)
    actor =models.TextField(null=True)

    def __repr__(self):
        return "<TopMovies:{} {}>".format(self.pk,self.rate)

    __str__=__repr__

