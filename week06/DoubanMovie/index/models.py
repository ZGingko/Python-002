from django.db import models

# Create your models here.


class Movie(models.Model):
    # Django会自动创建,并设置为主键
    id = models.AutoField(primary_key=True, db_column='Fid')
    name = models.CharField(max_length=100, db_column='Fname')
    year = models.CharField(max_length=4, db_column='Fyear')
    director = models.CharField(max_length=50, db_column='Fdirector')
    actors = models.CharField(max_length=200, db_column='Factors')
    categories = models.CharField(max_length=100, db_column='Fcategories')
    language = models.CharField(max_length=20, db_column='Flanguage')
    imdb_name = models.CharField(max_length=20, db_column='Fimdb_name')
    imdb_url = models.CharField(max_length=200, db_column='Fimdb_url')
    image_url = models.CharField(max_length=200, db_column='Fimage_url')

    class Meta:
        db_table = 't_movie'


class Comment(models.Model):
    id = models.AutoField(primary_key=True, db_column='Fid')
    author = models.CharField(max_length=20, db_column='Fauthor')
    content = models.CharField(max_length=1000, db_column='Fcontent')
    stars = models.IntegerField(db_column='Fstars')
    comment_time = models.CharField(max_length=20, db_column='Fcomment_time')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='Fmovie_id')

    class Meta:
        db_table = 't_comment'
        ordering = ['comment_time']
