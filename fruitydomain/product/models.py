from django.db import models

class fruits(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    price=models.IntegerField()
    qty=models.IntegerField()
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=('-date',)


class comment(models.Model):
    proid=models.ForeignKey(fruits,related_name='cmt',on_delete=models.CASCADE)
    user=models.CharField(max_length=100)
    msg=models.TextField()
    like=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)




# Create your models here.
