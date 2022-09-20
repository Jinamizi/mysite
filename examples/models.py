from django.db import models

from . import validators

class Example0(models.Model):
	even_field = models.IntegerField(validators=[validators.validate_even])

	def __str__(self):
		return str(self.even_field)

class  Place(models.Model):
	country = models.CharField(max_length=30, default = "Kenya")
	name = models.CharField('name of place', max_length=30, default='nairobi')
	zip_code = models.IntegerField(default=0)
		
class Person(models.Model):
	SHIRT_SIZES = (
		('S','Small'),
		('M', 'Medium'),
		('L', 'Large'),
	)
	name = models.CharField("person's first name", max_length=60) #use of verbose name
	shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

	#using enumeration classes to define choices in a concise way
	MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
	medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
	#place = models.OneToOneField(Place, on_delete=models.CASCADE, verbose_name='related place', default=Place())

	def __str__(self):
		return self.name

class Group(models.Model):
	name = models.CharField(max_length=128)
	members = models.ManyToManyField(Person, through='Membership')

	def __str__(self):
		return self.name

class Membership(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)
	date_joined = models.DateField()
	invite_reason = models.CharField(max_length=64)

#example of an abstract
class CommonInfo(models.Model):
		name = models.CharField(max_length=100)
		age = models.PositiveIntegerField()

		class Meta:
			abstract = True #This model will not be used to create any database table

		def __str__(self):
			return self.name

class Student(CommonInfo):
	FRESHMAN = 'FR'
	SOPHOMORE = 'SO'
	JUNIOR = 'JR'
	SENIOR = 'SR'
	GRADUATE = 'GR'
	home_group = models.CharField(max_length=5)
	YEAR_IN_SCHOOL_CHOICES = [
		(FRESHMAN, 'Freshman'),
		(SOPHOMORE, 'Sophomore'),
		(JUNIOR, 'Junior'),
		(SENIOR, 'Senior'),
		(GRADUATE, 'Graduate'),
	]
	year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES, default=FRESHMAN)

	def is_upperclass(self):
		return self.year_in_school in {self.JUNIOR, self.SENIOR}