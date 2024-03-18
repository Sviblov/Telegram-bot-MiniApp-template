CREATE DATABASE test_db;

DO $$
DECLARE 
    db_name text := 'test_db';
    db_user text := 'test_user';
    db_password text := 'test_password';
begin
    EXECUTE format('CREATE USER %I WITH PASSWORD %L', db_user, db_password);
    EXECUTE format('GRANT ALL PRIVILEGES ON DATABASE %I TO %I', db_name, db_user);
    EXECUTE format('ALTER DATABASE %I OWNER TO %I', db_name, db_user);
END $$;