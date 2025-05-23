CREATE DATABASE <db_name>;
CREATE USER <db_user_name> WITH PASSWORD '<db_password>';
ALTER ROLE <db_user_name> SET client_encoding TO 'utf8'; 
ALTER ROLE <db_user_name> SET default_transaction_isolation TO 'read committed'; 
ALTER ROLE <db_user_name> SET timezone TO 'UTC'; 
GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <db_user_name>; 
\c <db_name> postgres; 
grant all on schema public to <db_user_name>; 
\q # exit postgres cli
