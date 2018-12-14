import logging
import os
import pandas as pd
import sys as sys


def main(argv=None):
	"""
	Utilize Pandas library to read in both UNSD M49 country and area .csv file
	(tab delimited) as well as the UNESCO heritage site .csv file (tab delimited).
	Extract regions, sub-regions, intermediate regions, country and areas, and
	other column data.  Filter out duplicate values and NaN values and sort the
	series in alphabetical order. Write out each series to a .csv file for inspection.
	"""
	if argv is None:
		argv = sys.argv

	msg = [
		'Source file read {0}',
		'Hospital provider id written to file {0}',
		'Hospital name written to file {0}',
		'Hospital address written to file {0}',
		'Hospital city written to file {0}',
		'Hospital state written to file {0}',
		'Hospital zip code written to file {0}',
		'Hospital county name written to file {0}',
		'Hospital phone number written to file {0}',
		'Hospital payment measure name written to file {0}',
		'Hospital payment measure id written to file {0}',
		'Hospital payment measure category written to file {0}',
		'Hospital denominator written to file {0}',
		'Hospital payment written to file {0}',
		'Hospital lower estimate written to file {0}',
		'Hospital higher estimate written to file {0}',
		'Hospital payment footnote written to file {0}',
		'Hospital voc display name written to file {0}',
		'Hospital voc display id written to file {0}',
		'Hospital voc category written to file {0}',
		'Hospital voc footnote written to file {0}',
		'Hospital measure start date written to file {0}',
		'Hospital measure end date written to file {0}'
	]

	# Setting logging format and default level
	logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

	# Read in United Nations Statistical Division (UNSD) M49 Standard data set (tabbed separator)
	hospital_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/input/hospital_data_cut.csv'
	hospital_data_frame = read_csv(hospital_csv)
	logging.info(msg[0].format(os.path.abspath(hospital_csv)))

	# Write regions to a .csv file.
	hospital_provider_id = extract_filtered_series(hospital_data_frame, 'provider_identifier')
	hospital_provider_id_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/provider_id.csv'
	write_series_to_csv(hospital_provider_id, hospital_provider_id_csv, '\t', False)
	logging.info(msg[1].format(os.path.abspath(hospital_provider_id_csv)))

	# Write sub-regions to a .csv file.
	hospital_name = extract_filtered_series(hospital_data_frame, 'hospital_name')
	hospital_name_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_name.csv'
	write_series_to_csv(hospital_name, hospital_name_csv, '\t', False)
	logging.info(msg[2].format(os.path.abspath(hospital_name_csv)))

	# Write intermediate_regions to a .csv file.
	hospital_address = extract_filtered_series(hospital_data_frame, 'address')
	hospital_address_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_address.csv'
	write_series_to_csv(hospital_address, hospital_address_csv, '\t', False)
	logging.info(msg[3].format(os.path.abspath(hospital_address_csv)))

	# Write countries or areas to a .csv file.
	hospital_city = extract_filtered_series(hospital_data_frame, 'city')
	hospital_city_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_city.csv'
	write_series_to_csv(hospital_city, hospital_city_csv, '\t', False)
	logging.info(msg[4].format(os.path.abspath(hospital_city_csv)))

	# Write development status to a .csv file.
	hospital_state = extract_filtered_series(hospital_data_frame, 'state')
	hospital_state_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_state.csv'
	write_series_to_csv(hospital_state, hospital_state_csv, '\t', False)
	logging.info(msg[5].format(os.path.abspath(hospital_state_csv)))

	hospital_zip_code = extract_filtered_series(hospital_data_frame, 'zip_code')
	hospital_zip_code_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_zip_code.csv'
	write_series_to_csv(hospital_zip_code, hospital_zip_code_csv, '\t', False)
	logging.info(msg[6].format(os.path.abspath(hospital_zip_code_csv)))

	hospital_county = extract_filtered_series(hospital_data_frame, 'county')
	hospital_county_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_county.csv'
	write_series_to_csv(hospital_county, hospital_county_csv, '\t', False)
	logging.info(msg[7].format(os.path.abspath(hospital_county_csv)))

	hospital_phone = extract_filtered_series(hospital_data_frame, 'phone_number')
	hospital_phone_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_phone.csv'
	write_series_to_csv(hospital_phone, hospital_phone_csv, '\t', False)
	logging.info(msg[8].format(os.path.abspath(hospital_phone_csv)))

	hospital_payment_measure = extract_filtered_series(hospital_data_frame, 'payment_measure_name')
	hospital_payment_measure_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_payment_measure.csv'
	write_series_to_csv(hospital_payment_measure, hospital_payment_measure_csv, '\t', False)
	logging.info(msg[9].format(os.path.abspath(hospital_payment_measure_csv)))

	hospital_payment_measure_id = extract_filtered_series(hospital_data_frame, 'payment_measure_identifier')
	hospital_payment_measure_id_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_payment_measure_id.csv'
	write_series_to_csv(hospital_payment_measure_id, hospital_payment_measure_id_csv, '\t', False)
	logging.info(msg[10].format(os.path.abspath(hospital_payment_measure_id_csv)))

	hospital_payment_measure_category = extract_filtered_series(hospital_data_frame, 'payment_category_name')
	hospital_payment_measure_category_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_payment_measure_category.csv'
	write_series_to_csv(hospital_payment_measure_category, hospital_payment_measure_category_csv, '\t', False)
	logging.info(msg[11].format(os.path.abspath(hospital_payment_measure_category_csv)))

	hospital_denominator = extract_filtered_series(hospital_data_frame, 'denominator')
	hospital_denominator_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_denominator.csv'
	write_series_to_csv(hospital_denominator, hospital_denominator_csv, '\t', False)
	logging.info(msg[12].format(os.path.abspath(hospital_denominator_csv)))

	hospital_payment = extract_filtered_series(hospital_data_frame, 'payment_actual')
	hospital_payment_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_payment.csv'
	write_series_to_csv(hospital_payment, hospital_payment_csv, '\t', False)
	logging.info(msg[13].format(os.path.abspath(hospital_payment_csv)))

	hospital_lower_estimate = extract_filtered_series(hospital_data_frame, 'payment_estimate_lower')
	hospital_lower_estimate_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_lower_estimate.csv'
	write_series_to_csv(hospital_lower_estimate, hospital_lower_estimate_csv, '\t', False)
	logging.info(msg[14].format(os.path.abspath(hospital_lower_estimate_csv)))

	hospital_higher_estimate = extract_filtered_series(hospital_data_frame, 'payment_estimate_higher')
	hospital_higher_estimate_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_higher_estimate.csv'
	write_series_to_csv(hospital_higher_estimate, hospital_higher_estimate_csv, '\t', False)
	logging.info(msg[15].format(os.path.abspath(hospital_higher_estimate_csv)))

	hospital_payment_footnote = extract_filtered_series(hospital_data_frame, 'payment_footnote')
	hospital_payment_footnote_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_payment_footnote.csv'
	write_series_to_csv(hospital_payment_footnote, hospital_payment_footnote_csv, '\t', False)
	logging.info(msg[16].format(os.path.abspath(hospital_payment_footnote_csv)))

	hospital_voc_display_name = extract_filtered_series(hospital_data_frame, 'value_of_care_name')
	hospital_voc_display_name_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_voc_display_name.csv'
	write_series_to_csv(hospital_voc_display_name, hospital_voc_display_name_csv, '\t', False)
	logging.info(msg[17].format(os.path.abspath(hospital_voc_display_name_csv)))

	hospital_voc_display_id = extract_filtered_series(hospital_data_frame, 'value_of_care_identifier')
	hospital_voc_display_id_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_voc_display_id.csv'
	write_series_to_csv(hospital_voc_display_id, hospital_voc_display_id_csv, '\t', False)
	logging.info(msg[18].format(os.path.abspath(hospital_voc_display_id_csv)))

	hospital_voc_category = extract_filtered_series(hospital_data_frame, 'value_category_name')
	hospital_voc_category_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_voc_category.csv'
	write_series_to_csv(hospital_voc_category, hospital_voc_category_csv, '\t', False)
	logging.info(msg[19].format(os.path.abspath(hospital_voc_category_csv)))

	hospital_voc_footnote = extract_filtered_series(hospital_data_frame, 'value_footnote')
	hospital_voc_footnote_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_voc_footnote.csv'
	write_series_to_csv(hospital_voc_footnote, hospital_voc_footnote_csv, '\t', False)
	logging.info(msg[20].format(os.path.abspath(hospital_voc_footnote_csv)))

	hospital_measure_start_date = extract_filtered_series(hospital_data_frame, 'start_date')
	hospital_measure_start_date_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_measure_start_date.csv'
	write_series_to_csv(hospital_measure_start_date, hospital_measure_start_date_csv, '\t', False)
	logging.info(msg[21].format(os.path.abspath(hospital_measure_start_date_csv)))

	hospital_measure_end_date = extract_filtered_series(hospital_data_frame, 'start_date')
	hospital_measure_end_date_csv = '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_measure_end_date.csv'
	write_series_to_csv(hospital_measure_end_date, hospital_measure_end_date_csv, '\t', False)
	logging.info(msg[22].format(os.path.abspath(hospital_measure_end_date_csv)))



def extract_filtered_series(data_frame, column_name):
	"""
	Returns a filtered Panda Series one-dimensional ndarray from a targeted column.
	Duplicate values and NaN or blank values are dropped from the result set which is
	returned sorted (ascending).
	:param data_frame: Pandas DataFrame
	:param column_name: column name string
	:return: Panda Series one-dimensional ndarray
	"""
	return data_frame[column_name].drop_duplicates().dropna().sort_values()


def read_csv(path, delimiter=','):
	"""
	Utilize Pandas to read in *.csv file.
	:param path: file path
	:param delimiter: field delimiter
	:return: Pandas DataFrame
	"""
	return pd.read_csv(path, sep=delimiter, engine='python')


def write_series_to_csv(series, path, delimiter=',', row_name=True):
	"""
	Write Pandas DataFrame to a *.csv file.
	:param series: Pandas one dimensional ndarray
	:param path: file path
	:param delimiter: field delimiter
	:param row_name: include row name boolean
	"""
	series.to_csv(path, sep=delimiter, index=row_name)


if __name__ == '__main__':
	sys.exit(main())
