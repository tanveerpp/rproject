from django.db import models
class Emp(models.Model):
    ename=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    def __str__(self) -> str:
        return self.ename
