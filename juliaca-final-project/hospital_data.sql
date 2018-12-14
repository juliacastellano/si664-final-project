
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS state, zip_code, county, city, hospital,
  payment_measure, payment_category, hospital_payment, value, value_category, hospital_value;
SET FOREIGN_KEY_CHECKS=1;


CREATE TABLE IF NOT EXISTS state
  (
    state_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    state VARCHAR(45),
    PRIMARY KEY (state_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_state.csv'
INTO TABLE state
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (state);

CREATE TABLE IF NOT EXISTS zip_code
  (
    zip_code_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    zip_code VARCHAR(45),
    PRIMARY KEY (zip_code_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_zip_code.csv'
INTO TABLE zip_code
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (zip_code);


CREATE TABLE IF NOT EXISTS payment_measure
  (
    payment_measure_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    payment_measure_identifier VARCHAR(45),
    payment_measure_name VARCHAR(45),
    PRIMARY KEY (payment_measure_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_payment_measure.csv'
INTO TABLE payment_measure
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (payment_measure_identifier, payment_measure_name);

CREATE TABLE IF NOT EXISTS payment_category
  (
    payment_category_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    payment_category_name VARCHAR(45),
    PRIMARY KEY (payment_category_id)
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_payment_measure_category.csv'
INTO TABLE payment_category
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (payment_category_name);


CREATE TABLE IF NOT EXISTS value
  (
    value_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    value_of_care_identifier VARCHAR(45),
    value_of_care_name VARCHAR(45),
    PRIMARY KEY (value_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_voc_display_id.csv'
INTO TABLE value
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (value_of_care_identifier, value_of_care_name);


CREATE TABLE IF NOT EXISTS value_category
  (
    value_category_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    value_category_name VARCHAR(45),
    PRIMARY KEY (value_category_id)
   )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

LOAD DATA LOCAL INFILE '/Users/juliacastellano/Desktop/SI664/si664-final-project/output/hospital_voc_category.csv'
INTO TABLE value_category
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  (value_category_name);



CREATE TEMPORARY TABLE temp_hospital_data
  (
    id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    provider_identifier INTEGER,
    hospital_name VARCHAR(45),
    address VARCHAR(45),
    city VARCHAR(45),
    state VARCHAR(45),
    zip_code VARCHAR(45),
    county VARCHAR(45),
    phone_number VARCHAR(11),
    payment_measure_name VARCHAR(45),
    payment_measure_identifier VARCHAR(45),
    payment_category_name VARCHAR(45),
    denominator INTEGER,
    payment_actual DECIMAL,
    payment_estimate_lower DECIMAL,
    payment_estimate_higher DECIMAL,
    payment_footnote VARCHAR(100),
    value_of_care_name VARCHAR(45),
    value_of_care_identifier VARCHAR(45),
    value_category_name VARCHAR(45),
    value_footnote VARCHAR(100),
    start_date DATE,
    end_date DATE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;


LOAD DATA LOCAL INFILE '/Users/juliacastellano/Desktop/SI664/si664-final-project/input/hospital_data_cut.csv'
INTO TABLE temp_hospital_data
  CHARACTER SET utf8mb4
  FIELDS TERMINATED BY ','
  LINES TERMINATED BY '\n'
  IGNORE 1 LINES
  (provider_identifier,
  hospital_name,
  address,
  city,
  state,
  zip_code,
  county,
  phone_number,
  payment_measure_name,
  payment_measure_identifier,
  payment_category_name,
  denominator,
  payment_actual,
  payment_estimate_lower,
  payment_estimate_higher,
  payment_footnote,
  value_of_care_name,
  value_of_care_identifier,
  value_category_name,
  value_footnote,
  start_date,
  end_date)


  SET provider_identifier = IF(provider_identifier = '', NULL, provider_identifier),
  hospital_name = IF(hospital_name = '', NULL, TRIM(hospital_name)),
  address = IF(address = '', NULL, TRIM(address)),
  city = IF(city = '', NULL, TRIM(city)),
  state = IF(state = '', NULL, TRIM(state)),
  zip_code = IF(zip_code = '', NULL, zip_code),
  county = IF(county = '', NULL, TRIM(county)),
  phone_number = IF(phone_number = '', NULL, phone_number),
  payment_measure_name = IF(payment_measure_name = '', NULL, TRIM(payment_measure_name)),
  payment_measure_identifier = IF(payment_measure_identifier = '', NULL, payment_measure_identifier),
  payment_category_name = IF(payment_category_name = '', NULL, TRIM(payment_category_name)),
  denominator = IF(denominator = '', NULL, denominator),
  payment_actual = IF(payment_actual = '', NULL, payment_actual),
  payment_estimate_lower = IF(payment_estimate_lower = '', NULL, payment_estimate_lower),
  payment_estimate_higher = IF(payment_estimate_higher = '', NULL, payment_estimate_higher),
  payment_footnote = IF(payment_footnote = '', NULL, TRIM(payment_footnote)),
  value_of_care_name = IF(value_of_care_name = '', NULL, TRIM(value_of_care_name)),
  value_of_care_identifier = IF(value_of_care_identifier = '', NULL, value_of_care_identifier),
  value_category_name = IF(value_category_name = '', NULL, TRIM(value_category_name)),
  value_footnote = IF(value_footnote = '', NULL, TRIM(value_footnote)),
  start_date = IF(start_date = '', NULL, start_date),
  end_date = IF(end_date = '', NULL, end_date);


CREATE TABLE IF NOT EXISTS county
  (
    county_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    state_id INTEGER,
    county VARCHAR(45),
    PRIMARY KEY (county_id),
    FOREIGN KEY (state_id) REFERENCES state(state_id) ON DELETE RESTRICT
    ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO county
(state_id, county)
SELECT DISTINCT s.state_id, th.county
FROM temp_hospital_data th
LEFT JOIN state s
ON TRIM(th.state) = TRIM(s.state);


CREATE TABLE IF NOT EXISTS city
  (
    city_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    state_id INTEGER,
    city VARCHAR(45),
    PRIMARY KEY (city_id),
    FOREIGN KEY (state_id) REFERENCES state(state_id) ON DELETE RESTRICT
    ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO city
(state_id, city)
SELECT DISTINCT s.state_id, th.city
FROM temp_hospital_data th
LEFT JOIN state s
ON TRIM(th.state) = TRIM(s.state);


CREATE TABLE IF NOT EXISTS hospital
  (
    hospital_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    state_id INTEGER,
    county_id INTEGER,
    city_id INTEGER,
    zip_code_id INTEGER,
    provider_identifier INTEGER,
    hospital_name VARCHAR(45),
    address VARCHAR(45),
    phone_number VARCHAR(11),
    PRIMARY KEY (hospital_id),
    FOREIGN KEY (state_id) REFERENCES state(state_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (county_id) REFERENCES county(county_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (city_id) REFERENCES city(city_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (zip_code_id) REFERENCES zip_code(zip_code_id)
    ON DELETE RESTRICT ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO hospital
(state_id, county_id, city_id, zip_code_id, provider_identifier, hospital_name, address, phone_number)
SELECT DISTINCT s.state_id, co.county_id, ci.city_id, zc.zip_code_id, th.provider_identifier, th.hospital_name, th.address, th.phone_number
FROM temp_hospital_data th
LEFT JOIN state s
ON TRIM(th.state) = TRIM(s.state)
LEFT JOIN county co
ON TRIM(th.county) = TRIM(co.county)
AND TRIM(co.state_id) = TRIM(s.state_id)
LEFT JOIN city ci
ON TRIM(th.city) = TRIM(ci.city)
AND TRIM(ci.state_id) = TRIM(s.state_id)
LEFT JOIN zip_code zc
ON TRIM(th.zip_code) = TRIM(zc.zip_code);



CREATE TABLE IF NOT EXISTS hospital_payment
  (
    hospital_payment_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    hospital_id INTEGER,
    payment_measure_id INTEGER,
    payment_category_id INTEGER,
    denominator INTEGER,
    payment_actual DECIMAL,
    payment_estimate_lower DECIMAL,
    payment_estimate_higher DECIMAL,
    payment_footnote VARCHAR(100),
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (hospital_payment_id),
    FOREIGN KEY (hospital_id) REFERENCES hospital(hospital_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (payment_measure_id) REFERENCES payment_measure(payment_measure_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (payment_category_id) REFERENCES payment_category(payment_category_id)
    ON DELETE RESTRICT ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO hospital_payment
(hospital_id, payment_measure_id, payment_category_id, denominator, payment_actual, payment_estimate_lower,
  payment_estimate_higher, payment_footnote, start_date, end_date)
SELECT DISTINCT h.hospital_id, pm.payment_measure_id, pc.payment_category_id, th.denominator, th.payment_actual,
  th.payment_estimate_lower, th.payment_estimate_higher, th.payment_footnote, th.start_date, th.end_date
FROM temp_hospital_data th
LEFT JOIN hospital h
ON TRIM(th.hospital_name) = TRIM(h.hospital_name)
AND TRIM(th.address) = TRIM(h.address)
AND TRIM(th.provider_identifier) = TRIM(h.provider_identifier)
LEFT JOIN payment_measure pm
ON TRIM(th.payment_measure_identifier) = TRIM(pm.payment_measure_identifier)
LEFT JOIN payment_category pc
ON TRIM(th.payment_category_name) = TRIM(pc.payment_category_name);


CREATE TABLE IF NOT EXISTS hospital_value
  (
    hospital_value_id INTEGER NOT NULL AUTO_INCREMENT UNIQUE,
    hospital_id INTEGER,
    value_id INTEGER,
    value_category_id INTEGER,
    value_footnote VARCHAR(100),
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (hospital_value_id),
    FOREIGN KEY (hospital_id) REFERENCES hospital(hospital_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (value_id) REFERENCES value(value_id)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (value_category_id) REFERENCES value_category(value_category_id)
    ON DELETE RESTRICT ON UPDATE CASCADE
  )
ENGINE=InnoDB
CHARACTER SET utf8mb4
COLLATE utf8mb4_0900_ai_ci;

INSERT IGNORE INTO hospital_value
(hospital_id, value_id, value_category_id, value_footnote, start_date, end_date)
SELECT DISTINCT h.hospital_id, v.value_id, vc.value_category_id, th.value_footnote, th.start_date, th.end_date
FROM temp_hospital_data th
LEFT JOIN hospital h
ON TRIM(th.hospital_name) = TRIM(h.hospital_name)
AND TRIM(th.address) = TRIM(h.address)
AND TRIM(th.provider_identifier) = TRIM(h.provider_identifier)
LEFT JOIN value v
ON TRIM(th.value_of_care_identifier) = TRIM(v.value_of_care_identifier)
LEFT JOIN value_category vc
ON TRIM(th.value_category_name) = TRIM(vc.value_category_name);
