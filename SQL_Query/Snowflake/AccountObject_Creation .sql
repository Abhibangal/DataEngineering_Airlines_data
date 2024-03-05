--Create a storage integration with azure blob account.this is an account level object

CREATE STORAGE INTEGRATION AZUREBLOB_INT
TYPE  = EXTERNAL_STAGE
ENABLED = TRUE
STORAGE_PROVIDER = AZURE
AZURE_TENANT_ID = '740d81d4-e4d6-4689-8d63-22257ff4a74c'
STORAGE_ALLOWED_LOCATIONS = ('azure://abhiformula1dl.blob.core.windows.net/raw/' ,'azure://abhiformula1dl.blob.core.windows.net/iceberg/');


--Get the AZURE COnsent URL and provide consent from AZURE ADMIN for creation of Service Principle
DESC INTEGRATION AZUREBLOB_INT;

--- Grant a usage access on integration object to developer role for creating  external stage on blob 
grant usage on integration  AZUREBLOB_INT to role developer;
