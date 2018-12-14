# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class County(models.Model):
    county_id = models.AutoField(primary_key=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    county = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'county'


class Hospital(models.Model):
    hospital_id = models.AutoField(primary_key=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    county = models.ForeignKey(County, models.DO_NOTHING, blank=True, null=True)
    city = models.ForeignKey(City, models.DO_NOTHING, blank=True, null=True)
    zip_code = models.ForeignKey('ZipCode', models.DO_NOTHING, blank=True, null=True)
    provider_identifier = models.IntegerField(blank=True, null=True)
    hospital_name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospital'


class HospitalPayment(models.Model):
    hospital_payment_id = models.AutoField(primary_key=True)
    hospital = models.ForeignKey(Hospital, models.DO_NOTHING, blank=True, null=True)
    payment_measure = models.ForeignKey('PaymentMeasure', models.DO_NOTHING, blank=True, null=True)
    payment_category = models.ForeignKey('PaymentCategory', models.DO_NOTHING, blank=True, null=True)
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
    hospital = models.ForeignKey(Hospital, models.DO_NOTHING, blank=True, null=True)
    value = models.ForeignKey('Value', models.DO_NOTHING, blank=True, null=True)
    value_category = models.ForeignKey('ValueCategory', models.DO_NOTHING, blank=True, null=True)
    value_footnote = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospital_value'


class PaymentCategory(models.Model):
    payment_category_id = models.AutoField(primary_key=True)
    payment_category_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_category'


class PaymentMeasure(models.Model):
    payment_measure_id = models.AutoField(primary_key=True)
    payment_measure_identifier = models.CharField(max_length=45, blank=True, null=True)
    payment_measure_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_measure'


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'


class Value(models.Model):
    value_id = models.AutoField(primary_key=True)
    value_of_care_identifier = models.CharField(max_length=45, blank=True, null=True)
    value_of_care_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'value'


class ValueCategory(models.Model):
    value_category_id = models.AutoField(primary_key=True)
    value_category_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'value_category'


class ZipCode(models.Model):
    zip_code_id = models.AutoField(primary_key=True)
    zip_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zip_code'
