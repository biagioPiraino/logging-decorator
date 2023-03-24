CREATE DATABASE logging_decorator;

\c logging_decorator;

CREATE TABLE logging (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    method_name TEXT NOT NULL,
    username TEXT NOT NULL,
    authenticated BOOLEAN
);

CREATE OR REPLACE FUNCTION log_method_call(
    method_name TEXT,
    username TEXT,
    authenticated BOOLEAN
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO logging (method_name, username, authenticated)
    VALUES (
      method_name,
      username,
      authenticated
    );
END;
$$ LANGUAGE plpgsql;