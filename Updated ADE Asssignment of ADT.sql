SELECT datname FROM pg_database;

SELECT current_database();

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'; -- Replace 'public' with your schema if needed




CREATE TYPE pan_number AS (
    first_five_chars CHAR(5),
    next_four_digits INTEGER,
    last_char CHAR(1)
);


CREATE TABLE employees (
    empid SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INTEGER,
    photo BYTEA,
    pan_num_data pan_number
);


INSERT INTO employees (name, age, photo, pan_num_data)
VALUES 
    ('Rajesh Khanna', 30, E'\\xDEADBEEF', ROW('ABCDE', 1234, 'F')),
    ('Amitabh Bacchan', 32, E'\\xDEACBEEE', ROW('FYXTA', 6542, 'C')),
    ('Dilip Kumar', 35, E'\\xDEAFBEEE', ROW('QWERT', 9876, 'D')),
    ('Mohanlal', 40, E'\\xDEAEBAEE', ROW('ZXCVB', 4567, 'G'));


SELECT * FROM employees;

SELECT
    empid,
    name,
    age,
    photo,
    (pan_num_data).first_five_chars || (pan_num_data).next_four_digits || (pan_num_data).last_char AS pan_number
FROM
    employees;






-- ADT for image storage
CREATE TYPE ImageStorage AS (
    image_id INTEGER,
    image_name TEXT,
    image_data BYTEA,
    upload_date TIMESTAMP
);

-- Table for storing images
CREATE TABLE ImageStorageTable (
    image ImageStorage
);

-- Inserting an example image into the ImageStorageTable
INSERT INTO ImageStorageTable (image) VALUES (
    ROW(1, 'example_image.jpg', decode('FFD8FFE000104A46494600010101006000600000FFE101184578696600004D4D002A000000080006011A0005000000010000000000010002000900000003000000010000000100000001000000010000', 'hex'), CURRENT_TIMESTAMP)
);

-- Function to retrieve an image by its ID
CREATE FUNCTION get_image_by_id(image_id INTEGER) RETURNS ImageStorage AS
$$
DECLARE
    image_info ImageStorage;
BEGIN
    SELECT image
    INTO image_info
    FROM ImageStorageTable
    WHERE image.image_id = get_image_by_id.image_id;
    RETURN image_info;
END;
$$ LANGUAGE plpgsql;
SELECT (image).image_data
FROM ImageStorageTable
WHERE (image).image_id = 1;

--docker run --name postgres-db -p 5432:5432 -e POSTGRES_USER=user_demo -e POSTGRES_PASSWORD=pg_strong_password -e POSTGRES_DB=demo_db postgres