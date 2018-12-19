from si664finalproject.models import City, County, Hospital, \
	HospitalPayment, HospitalValue, PaymentCategory, PaymentMeasure, State, \
	Value, ValueCategory, ZipCode
from rest_framework import response, serializers, status

class StateSerializer(serializers.ModelSerializer):

	class Meta:
		model = State
		fields = ('state_id', 'state')

class ZipCodeSerializer(serializers.ModelSerializer):

	class Meta:
		model = ZipCode
		fields = ('zip_code_id', 'zip_code')

class CitySerializer(serializers.ModelSerializer):
	state = StateSerializer(many=False, read_only=True)

	class Meta:
		model = City
		fields = ('city_id', 'state', 'city')


class CountySerializer(serializers.ModelSerializer):
	state = StateSerializer(many=False, read_only=True)

	class Meta:
		model = County
		fields = ('county_id', 'state', 'county')


class PaymentCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = PaymentCategory
		fields = ('payment_category_id', 'payment_category_name')


class PaymentMeasureSerializer(serializers.ModelSerializer):

	class Meta:
		model = PaymentMeasure
		fields = ('payment_measure_id', 'payment_measure_identifier', 'payment_measure_name')


class ValueSerializer(serializers.ModelSerializer):

	value_of_care_identifier = serializers.CharField(
		allow_null=False
	)

	value_of_care_name = serializers.CharField(
		allow_null=False
	)


	class Meta:
		model = Value
		fields = (
			'value_id',
			'value_of_care_identifier',
			'value_of_care_name',
		)

	def create(self, validated_data):

		value = Value.objects.create(**validated_data)

		return value

	def update(self, instance, validated_data):
		value_id = instance.value_id

		instance.value_of_care_identifier = validated_data.get(
			'value_of_care_identifier',
			instance.value_of_care_identifier
		)

		instance.value_of_care_name = validated_data.get(
			'value_of_care_name',
			instance.value_of_care_name
		)

		instance.save()

		return instance


class ValueCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = ValueCategory
		fields = ('value_category_id', 'value_category_name')


class HospitalSerializer(serializers.ModelSerializer):
	state = StateSerializer(
		many=False,
		read_only=True
	)

	county = CountySerializer(
		many=False,
		read_only=True
	)

	city = CitySerializer(
		many=False,
		read_only=True
	)

	zip_code = ZipCodeSerializer(
		many=False,
		read_only=True
	)

	provider_identifier = serializers.IntegerField(
		allow_null=True
	)

	hospital_name = serializers.CharField(
		allow_null=False
	)

	address = serializers.CharField(
		allow_null=True
	)

	phone_number = serializers.IntegerField(
		allow_null=True
	)


	class Meta:
		model = Hospital
		fields = (
			'hospital_id',
			'state',
			'county',
			'city',
			'zip_code',
			'provider_identifier',
			'hospital_name',
			'address',
			'phone_number',
		)

	def create(self, validated_data):

		hospital = Hospital.objects.create(**validated_data)

		return hospital

	def update(self, instance, validated_data):
		# site_id = validated_data.pop('heritage_site_id')
		hospital_id = instance.hospital_id

		instance.provider_identifier = validated_data.get(
			'provider_identifier',
			instance.provider_identifier
		)

		instance.hospital_name = validated_data.get(
			'hospital_name',
			instance.hospital_name
		)

		instance.address = validated_data.get(
			'address',
			instance.address
		)
		instance.phone_number = validated_data.get(
			'phone_number',
			instance.phone_number
		)

		instance.save()

		return instance

class HospitalValueSerializer(serializers.ModelSerializer):
	hospital_id = serializers.PrimaryKeyRelatedField(
		allow_null=False,
		many=False,
		write_only=True,
		queryset=Hospital.objects.all(),
		source='hospital'
	)

	value_id = serializers.PrimaryKeyRelatedField(
		allow_null=False,
		many=False,
		write_only=True,
		queryset=Value.objects.all(),
		source='value'
	)

	value_category_id = serializers.PrimaryKeyRelatedField(
		allow_null=False,
		many=False,
		write_only=True,
		queryset=ValueCategory.objects.all(),
		source='value_category'
	)

	value_footnote = serializers.CharField(
		allow_null=False
	)

	start_date = serializers.DateField(
		allow_null=False
	)

	end_date = serializers.DateField(
		allow_null=False
	)


	class Meta:
		model = HospitalValue
		fields = (
			'hospital_value_id',
			'hospital_id',
			'value_id',
			'value_category_id',
			'value_footnote',
			'start_date',
			'end_date',
		)

	def create(self, validated_data):

		hospital_value = HospitalValue.objects.create(**validated_data)

		return hospital_value

	def update(self, instance, validated_data):
		hospital_value_id = instance.hospital_value_id

		instance.hospital_id = validated_data.get(
			'hospital_id',
			instance.hospital_id
		)

		instance.value_id = validated_data.get(
			'value_id',
			instance.value_id
		)

		instance.value_category_id = validated_data.get(
			'value_category_id',
			instance.value_category_id
		)

		instance.value_footnote = validated_data.get(
			'value_footnote',
			instance.value_footnote
		)

		instance.start_date = validated_data.get(
			'start_date',
			instance.start_date
		)

		instance.end_date = validated_data.get(
			'end_date',
			instance.end_date
		)

		instance.save()

		return instance
