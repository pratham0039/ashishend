from django.db import models


class Record(models.Model):
	tests = models.ManyToManyField('Test', related_name='records')
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)

	lab = models.CharField(max_length=50, default='own')
	
	total_price = models.IntegerField(default = 0)
	paid = models.CharField(max_length=50, default='paid')


	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
	
class Test(models.Model):
	code = models.CharField(max_length = 10)
	testname = models.CharField(max_length = 50)
	Price = models.IntegerField()

	def __str__(self):
           return self.testname
	


class LabDeposit(models.Model):
    lab = models.CharField(max_length = 50)
    deposit = models.IntegerField()
