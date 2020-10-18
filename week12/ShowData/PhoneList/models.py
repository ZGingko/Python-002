from django.db import models


class Comments(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='Fid')
    phone_title = models.CharField(max_length=255, db_column='Fphone_title')
    alink = models.CharField(max_length=255, blank=True,
                             null=True, db_column='Falink')
    user_name = models.CharField(max_length=255, db_column='Fuser_name')
    comment = models.TextField(db_column='Fcomment')
    sentiments = models.FloatField(db_column='Fsentiments')
    create_time = models.DateTimeField(db_column='Fcreate_time')

    class Meta:
        managed = False
        db_table = 't_phone_comments'
