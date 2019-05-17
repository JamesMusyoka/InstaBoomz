from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Images(models.Model):
	name = models.CharField(max_length =30)
	caption = models.CharField(max_length =150, default="")
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name="red")
	likes = models.IntegerField(default=0)
	comment = models.CharField(max_length=150)
	pub_date = models.DateTimeField(auto_now_add=True)




	def __str__(self):
	        return self.name