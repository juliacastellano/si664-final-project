import django_filters
from si664finalproject.models import City, County, Hospital, \
	HospitalPayment, HospitalValue, PaymentCategory, PaymentMeasure, State, \
	Value, ValueCategory, ZipCode


class si664finalprojectFilter(django_filters.FilterSet):
	hospital_name = django_filters.CharFilter(
		field_name='hospital_name',
		label='Hospital Name',
		lookup_expr='icontains'
	)

	city = django_filters.ModelChoiceFilter(
		field_name='city',
		label='City',
		queryset=City.objects.all().order_by('city'),
		lookup_expr='exact'
	)

	county = django_filters.ModelChoiceFilter(
		field_name='county',
		label='County',
		queryset=County.objects.all().order_by('county'),
		lookup_expr='exact'
	)

	state = django_filters.ModelChoiceFilter(
		field_name='state',
		label='State',
		queryset=State.objects.all().order_by('state'),
		lookup_expr='exact'
	)

	zip_code = django_filters.ModelChoiceFilter(
		field_name='zip_code',
		label='Zip Code',
		queryset=ZipCode.objects.all().order_by('zip_code'),
		lookup_expr='exact'
	)

	payment_category_name = django_filters.ModelChoiceFilter(
		field_name='payment_category_name',
		label='Payment Category',
		queryset=PaymentCategory.objects.all().order_by('payment_category_name'),
		lookup_expr='exact'
	)

	value_category_name = django_filters.ModelChoiceFilter(
		field_name='value_category_name',
		label='Value Category',
		queryset=ValueCategory.objects.all().order_by('value_category_name'),
		lookup_expr='exact'
	)


	class Meta:
		model = Hospital
		# form = SearchForm
		# fields [] is required, even if empty.
		fields = []