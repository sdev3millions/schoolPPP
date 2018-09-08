from django.db import models
from datetime import datetime
# Create your models here.
class Schools(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now,blank=True)
    class Meta:
        db_table="school_schools"
class SchoolData(models.Model):
    school_id=models.IntegerField()
    year=models.IntegerField()
    month=models.IntegerField()
    week= models.IntegerField()
    ele_k=models.IntegerField()
    ele_u=models.IntegerField()
    hea_k=models.IntegerField()
    hea_u=models.IntegerField()
    wat_l=models.IntegerField()
    wat_u=models.IntegerField()
    created_at=models.DateTimeField(default=datetime.now,blank=True)
    class Meta:
        db_table="school_schooldata"
    
    