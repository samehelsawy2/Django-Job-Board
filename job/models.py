from django.db import models


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
# Create your models here.
class job(models.Model): # tabel
    title = models.CharField(max_length=100) # column
    #location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    puplished_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    def __str__(self):
        return self.title
