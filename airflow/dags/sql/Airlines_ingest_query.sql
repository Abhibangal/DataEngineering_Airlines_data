Truncate  table {{ params.database_name }}.{{ params.schema_name }}.airlines_stg;
copy into {{ params.database_name }}.{{ params.schema_name }}.airlines_stg from 
                                @{{ params.database_name }}.{{ params.schema_name }}.TEST_AIRLINES_BLOB_STG/Airlines_Data.csv.gz
                                            file_format = '{{ params.database_name }}.{{ params.schema_name }}.AIRLINES_CSV_FORMAT',
                                            ON_ERROR = ABORT_STATEMENT ,
                                            force = FALSE;
                                            