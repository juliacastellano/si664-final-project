# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse

class City(models.Model):
	city_id = models.AutoField(primary_key=True)
	state = models.ForeignKey('State', on_delete=models.PROTECT, blank=True, null=True)
	city = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'city'

	def __str__(self):
		return str(self.city)


class County(models.Model):
	county_id = models.AutoField(primary_key=True)
	state = models.ForeignKey('State', on_delete=models.PROTECT, blank=True, null=True)
	county = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'county'

	def __str__(self):
		return str(self.county)

class PaymentCategory(models.Model):
	payment_category_id = models.AutoField(primary_key=True)
	payment_category_name = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'payment_category'

	def __str__(self):
		return str(self.payment_category_name)


class PaymentMeasure(models.Model):
	payment_measure_id = models.AutoField(primary_key=True)
	payment_measure_identifier = models.CharField(max_length=45, blank=True, null=True)
	payment_measure_name = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'payment_measure'

	def __str__(self):
		return str(self.payment_measure_name)


class State(models.Model):
	state_id = models.AutoField(primary_key=True)
	state = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'state'

	def __str__(self):
		return str(self.state)


class Value(models.Model):
	value_id = models.AutoField(primary_key=True)
	value_of_care_identifier = models.CharField(max_length=45, blank=True, null=True)
	value_of_care_name = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'value'

	def __str__(self):
		return str(self.value_of_care_name)


class ValueCategory(models.Model):
	value_category_id = models.AutoField(primary_key=True)
	value_category_name = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'value_category'

	def __str__(self):
		return str(self.value_category_name)


class ZipCode(models.Model):
	zip_code_id = models.AutoField(primary_key=True)
	zip_code = models.CharField(max_length=45, blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'zip_code'

	def __str__(self):
		return str(self.zip_code)


class Hospital(models.Model):
	hospital_id = models.AutoField(primary_key=True)
	state = models.ForeignKey('State', on_delete=models.PROTECT, blank=True, null=True)
	county = models.ForeignKey('County', on_delete=models.PROTECT, blank=True, null=True)
	city = models.ForeignKey('City', on_delete=models.PROTECT, blank=True, null=True)
	zip_code = models.ForeignKey('ZipCode', on_delete=models.PROTECT, blank=True, null=True)
	provider_identifier = models.IntegerField(blank=True, null=True)
	hospital_name = models.CharField(max_length=45, blank=True, null=True)
	address = models.CharField(max_length=45, blank=True, null=True)
	phone_number = models.CharField(max_length=11, blank=True, null=True)

	payment_measure = models.ManyToManyField(PaymentMeasure, through='HospitalPayment')
	payment_category = models.ManyToManyField(PaymentCategory, through='HospitalPayment')

	value = models.ManyToManyField(Value, through='HospitalValue')
	value_category = models.ManyToManyField(ValueCategory, through='HospitalValue')


	class Meta:
		managed = False
		db_table = 'hospital'

	def __str__(self):
		return str(self.hospital_name)

	def get_absolute_url(self):
		return reverse('hospital_detail', kwargs={'pk': self.pk})

	@property
	def payment_category_names(self):
		# Add code that uses self to retrieve a QuerySet composed of regions, then loops over it
		# building a list of region names, before returning a comma-delimited string of names.
		payment_categories = self.payment_category.all()

		names = []
		for payment_category in payment_categories:
			payment_category = payment_category
			if payment_category is None:
				name = 'Missing'
			name = payment_category.payment_category_name
			names.append(name)


		payment_measures = self.payment_measure.all()

		names2 = []
		for payment_measure in payment_measures:
			payment_measure = payment_measure
			if payment_measure is None:
				name = 'Missing'
			name = payment_measure.payment_measure_name
			names2.append(name)

		names3 = []
		for val1, val2 in zip(names, names2):
			joined = ''.join([val2.strip(), ': ', val1.strip()])
			if joined not in names3:
				names3.append(joined)

		return '; '.join(names3)


	@property
	def value_names(self):

		# Add code that uses self to retrieve a QuerySet, then loops over it building a list of
		# intermediate region names, before returning a comma-delimited string of names using the
		# string join method.
		values = self.value.all()

		names = []
		for value in values:
			value = value
			if value is None:
				name = 'Missing'
			name = value.value_of_care_name
			if name not in names:
				names.append(name)

		value_categories = self.value_category.all()

		names2 = []
		for value_category in value_categories:
			value_category = value_category
			if value_category is None:
				name = 'Missing'
			name = value_category.value_category_name
			if name not in names2:
				names2.append(name)

		names3 = []
		for val1, val2 in zip(names, names2):
			joined = ''.join([val1.strip(), ': ', val2.strip()])
			if joined not in names3:
				names3.append(joined)

		return '; '.join(names3)



class HospitalPayment(models.Model):
	hospital_payment_id = models.AutoField(primary_key=True)
	hospital = models.ForeignKey('Hospital', on_delete=models.PROTECT, blank=True, null=True)
	payment_measure = models.ForeignKey('PaymentMeasure', on_delete=models.PROTECT, blank=True, null=True)
	payment_category = models.ForeignKey('PaymentCategory', on_delete=models.PROTECT, blank=True, null=True)
	denominator = models.IntegerField(blank=True, null=True)
	payment_actual = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	payment_estimate_lower = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	payment_estimate_higher = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
	payment_footnote = models.CharField(max_length=100, blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'hospital_payment'



class HospitalValue(models.Model):
	hospital_value_id = models.AutoField(primary_key=True)
	hospital = models.ForeignKey('Hospital', on_delete=models.PROTECT, blank=True, null=True)
	value = models.ForeignKey('Value', on_delete=models.PROTECT, blank=True, null=True)
	value_category = models.ForeignKey('ValueCategory', on_delete=models.PROTECT, blank=True, null=True)
	value_footnote = models.CharField(max_length=100, blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	end_date = models.DateField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'hospital_value'
