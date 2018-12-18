create database if not exists hospital_data;

use hospital_data;

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS state, zip_code, county, city, hospital,
  payment_measure, payment_category, hospital_payment, value, value_category, hospital_value;
SET FOREIGN_KEY_CHECKS=1;
