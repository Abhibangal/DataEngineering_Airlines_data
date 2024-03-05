-- Create a database and schema using accountadmin roll
Use role AccountAdmin;
create database test_analytics;
create schema airlines;

-- Grant the ownership and all privilieges of the database to Sysadmin 
grant ownership  on database test_analytics to role sysadmin revoke current grants;
grant all privileges on future schemas in database test_analytics to role sysadmin with grant option;
grant all privileges on future stages in schema airlines to role sysadmin with grant option;
grant all privileges on future file formats in schema airlines to role sysadmin with grant option;

-- Create a new user  using USERADMIN and assign the Role Developer Role using SecurityAdmin 
use role sysadmin;
use database test_analytics;

--Grant Usage access to new DEVELOPER role on Database ,Schema and Warehouse
grant usage on database test_analytics to role developer;
grant usage on schema airlines to role developer;
grant usage on warehouse compute_wh to role developer;

-- Grant Objectprivileges to Role developer
grant create schema  on database test_analytics to role developer;
grant create table on schema airlines to role developer;
grant create external table  on schema airlines to role developer;
grant create iceberg table  on schema airlines to role developer;
grant create  view on schema airlines to role developer;
grant create file format  on schema airlines to role developer;
grant create stage  on schema airlines to role developer;
grant create task  on schema airlines to role developer;
grant create stream  on schema airlines to role developer;
grant create pipe  on schema airlines to role developer;

GRANT MODIFY ON SCHEMA AIRLINES TO ROLE DEVELOPER;

show grants to role developer;



show grants to role sysadmin;