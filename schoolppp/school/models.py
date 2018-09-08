from django.db import models

# Create your models here.
class Schools(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    class Meta:
        db_table="school_schools"
class SchoolData(models.Model):
    school_id=models.IntegerField()
    ele_k=models.IntegerField()
    ele_u=models.IntegerField()
    hea_k=models.IntegerField()
    hea_u=models.IntegerField()
    wat_l=models.IntegerField()
    wat_u=models.IntegerField()
    class Meta:
        db_table="school_schooldata"
    
    