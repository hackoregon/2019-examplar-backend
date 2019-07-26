from django.db import models

class RouteChange(models.Model):
    route_id = models.TextField(primary_key=True)
    shape_id = models.TextField(blank=True, null=True)
    y2009_trip_count = models.IntegerField(blank=True, null=True)
    y2017_trip_count = models.IntegerField(blank=True, null=True)
    pct_change = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'route_change'
