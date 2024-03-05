MERGE INTO {{ params.database_name }}.{{ params.schema_name }}.OBT_AIRLINES T
	USING {{ params.database_name }}.{{ params.schema_name }}.AIRLINES_STG S
		ON T.PASSENGER_ID = S."passenger_id"
		AND T.DEPARTURE_DT = TO_DATE(S."Departure_Date")
		AND T.ARRIVAL_AIRPORT = S."Arrival_Airport"
	WHEN MATCHED THEN UPDATE
		SET 
			T.PASSENGER_ID    = S."passenger_id",
			T.FIRST_NAME= S."First_name",
			T.LAST_NAME= S."Last_name",
			T.GENDER= S."Gender",
			T.AGE = S."Age",
			T.NATIONALITY= S."Nationality",
			T.AIRPORT_NAME= S."Airport_name",
			T.COUNTRY_NAME= S."Country_Name",
			T.CONTINENTS= S."Continents",
			T.DEPARTURE_DT = S."Departure_Date",
			T.ARRIVAL_AIRPORT= S."Arrival_Airport",
			T.PILOT_NAME = S."Pilot_Name",
			T.FLIGHT_STATUS = S."Flight_Status"
	WHEN NOT MATCHED THEN INSERT 
		VALUES(S."passenger_id",
			S."First_name",
			S."Last_name",
			S."Gender",
			S."Age",
			S."Nationality",
			S."Airport_name",
			S."Country_Name",
			S."Continents",
			S."Departure_Date",
			S."Arrival_Airport",
			S."Pilot_Name",
			S."Flight_Status")
;
			