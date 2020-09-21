from django.db import models


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
# Create your models here.
def image_upload(instance,filename):
    imagename,extention = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extention)



class job(models.Model): # tabel
    title = models.CharField(max_length=100) # column
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    puplished_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name