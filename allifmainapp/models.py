from django.db import models

# Create your models here.
class namesmodel(models.Model):
    name=models.CharField(max_length=200,blank=True,null=True)
    myimage=models.ImageField(upload_to='amel/images/names/%Y/',null=True, blank=True)#
    mydocument=models.FileField(upload_to='allifmaal/files/',blank=True,null=True)
      
    def __str__(self):
        return self.name
