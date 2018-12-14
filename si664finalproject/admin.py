from django.contrib import admin
import si664finalproject.models as models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
	fields = ['state', 'city']
	list_display = ['state', 'city']
	ordering = ['city']



@admin.register(models.County)
class CountyAdmin(admin.ModelAdmin):
	fields = ['state', 'county']
	list_display = ['state', 'county']
	ordering = ['county']



@admin.register(models.Hospital)
class HospitalAdmin(admin.ModelAdmin):
	fields = [
		'state',
		'county',
		'city',
		'zip_code',
		'provider_identifier',
		'hospital_name',
		'address',
		'phone_number'
	]

	list_display = (
		'state',
		'county',
		'city',
		'zip_code',
		'provider_identifier',
		'hospital_name',
		'address',
		'phone_number'
	)

	list_filter = (
		'state',
		'county',
		'city',
		'zip_code',
		'provider_identifier',
		'hospital_name',
		'address',
		'phone_number'
	)



@admin.register(models.HospitalPayment)
class HospitalPaymentAdmin(admin.ModelAdmin):
	fields = [
		'hospital',
		'payment_measure',
		'payment_category',
		'denominator',
		'payment_actual',
		'payment_estimate_lower',
		'payment_estimate_higher',
		'payment_footnote',
		'start_date',
		'end_date'
	]

	list_display = [
		'hospital',
		'payment_measure',
		'payment_category',
		'denominator',
		'payment_actual',
		'payment_estimate_lower',
		'payment_estimate_higher',
		'payment_footnote',
		'start_date',
		'end_date'
	]

	list_filter = [
		'hospital',
		'payment_measure',
		'payment_category',
		'denominator',
		'payment_actual',
		'payment_estimate_lower',
		'payment_estimate_higher',
		'payment_footnote',
		'start_date',
		'end_date'
	]



@admin.register(models.HospitalValue)
class HospitalValueAdmin(admin.ModelAdmin):
	fields = [
		'hospital',
		'value',
		'value_category',
		'value_footnote',
		'start_date',
		'end_date'
	]
	list_display = [
		'hospital',
		'value',
		'value_category',
		'value_footnote',
		'start_date',
		'end_date'
	]
	list_filter = [
		'hospital',
		'value',
		'value_category',
		'value_footnote',
		'start_date',
		'end_date'
	]


@admin.register(models.PaymentCategory)
class PaymentCategoryAdmin(admin.ModelAdmin):
	fields = ['payment_category_name']
	list_display = ['payment_category_name']
	ordering = ['payment_category_name']



@admin.register(models.PaymentMeasure)
class PaymentMeasureAdmin(admin.ModelAdmin):
	fields = ['payment_measure_identifier', 'payment_measure_name']
	list_display = ['payment_measure_identifier', 'payment_measure_name']
	ordering = ['payment_measure_name']


@admin.register(models.State)
class State(admin.ModelAdmin):
	fields = ['state']
	list_display = ['state']
	ordering = ['state']


@admin.register(models.Value)
class Value(admin.ModelAdmin):
	fields = ['value_of_care_identifier', 'value_of_care_name']
	list_display = ['value_of_care_identifier', 'value_of_care_name']
	ordering = ['value_of_care_name']


@admin.register(models.ValueCategory)
class ValueCategory(admin.ModelAdmin):
	fields = ['value_category_name']
	list_display = ['value_category_name']
	ordering = ['value_category_name']


@admin.register(models.ZipCode)
class ZipCode(admin.ModelAdmin):
	fields = ['zip_code']
	list_display = ['zip_code']
	ordering = ['zip_code']
