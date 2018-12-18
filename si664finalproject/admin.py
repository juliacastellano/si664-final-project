from django.contrib import admin
import si664finalproject.models as models


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
	fields = ['city']
	list_display = ['city']
	ordering = ['city']



@admin.register(models.County)
class CountyAdmin(admin.ModelAdmin):
	fields = ['county']
	list_display = ['county']
	ordering = ['county']



@admin.register(models.Hospital)
class HospitalAdmin(admin.ModelAdmin):
	fields = [
		'provider_identifier',
		'hospital_name',
		'address',
		'phone_number'
	]

	list_display = (
		'provider_identifier',
		'hospital_name',
		'address',
		'phone_number'
	)

	list_filter = (
		'provider_identifier',
		'hospital_name',
		'address',
		'phone_number'
	)



@admin.register(models.HospitalPayment)
class HospitalPaymentAdmin(admin.ModelAdmin):
	fields = [
		'denominator',
		'payment_actual',
		'payment_estimate_lower',
		'payment_estimate_higher',
		'payment_footnote',
		'start_date',
		'end_date'
	]

	list_display = [
		'denominator',
		'payment_actual',
		'payment_estimate_lower',
		'payment_estimate_higher',
		'payment_footnote',
		'start_date',
		'end_date'
	]

	list_filter = [
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
		'value_footnote',
		'start_date',
		'end_date'
	]
	list_display = [
		'value_footnote',
		'start_date',
		'end_date'
	]
	list_filter = [
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
