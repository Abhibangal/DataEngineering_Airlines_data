--Create a schema as below 
create schema dataengineer;
-- use it 
use  dataengineer;

-- Bulk loading of data from file 
-- Wanted to create ODS system which will have data loaded from file.
LOAD DATA INFILE "C://ProgramData//MySQL//MySQL Server 8.0//Uploads//Airline_splited_files//Airline_dataset_1.csv" INTO TABLE dataengineer.ods_airlines 
FIELDS TERMINATED BY ','
ENCLOSED by '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 LINES;

--rename the column which have space in their name for future convience 
alter table dataengineer.ods_airlines 
rename column `Passenger ID` to Passenger_Id,
rename column `First Name` to First_name,
rename column `Last Name` to Last_name,
rename column `Airport Name` to Airport_name,
rename column `Airport Country Code` to Airport_Country_Code,
rename column `Country Name` to Country_Name,
rename column `Airport Continent` to Airport_Continent,
rename column `Departure Date` to Departure_Date,
rename column `Arrival Airport` to Arrival_Airport,
rename column `Pilot Name` to Pilot_Name,
rename column `Flight Status` to Flight_Status
;


