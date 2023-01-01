from django.contrib.auth.models import User
from django.db import models
from main.models import customUser
# Create your models here.
class jobs(models.Model):
    idemployer = models.ForeignKey(customUser,on_delete = models.CASCADE,related_name='+')
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="static/jobs")
    status = models.CharField(max_length=50)
    countem = models.IntegerField()
    
    def __str__(self):
        return self.title

class sabtjob(models.Model):
    id_emploee = models.ForeignKey(customUser,on_delete = models.CASCADE,related_name='+')
    vaziat = models.CharField(max_length=25,blank=True,null=True)
    id_employer = models.ForeignKey(User,on_delete = models.CASCADE)
    id_job = models.ForeignKey(jobs,on_delete = models.CASCADE)
    def __str__(self):
	    return self.id_job.title