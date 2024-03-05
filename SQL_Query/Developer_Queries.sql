use test_analytics.airlines;

--Since our container raw/csv on which we are creating the stage only stores CSV file so we will be setting file format at Stage level.
--Create a file format
create or replace file format airlines_csv_format
type = CSV
compression = gzip
skip_header = 1
FIELD_OPTIONALLY_ENCLOSED_BY = '"'
EMPTY_FIELD_AS_NULL = TRUE
trim_space = True;


-- Create an external stage test_airlines_blob_stg
create or replace stage test_airlines_blob_stg
url = 'azure://abhiformula1dl.blob.core.windows.net/raw/csv/'
storage_integration = AZUREBLOB_INT
file_format = airlines_csv_format;



show grants to role developer;
