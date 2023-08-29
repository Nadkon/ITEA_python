/*
CREATE table "user" (
  id  Serial PRIMARY KEY,
  name varchar(50),
  surname VARCHAR(70),
  phone VARCHAR(15),
  email varchar(50)
);
*/
--ALTER table "user" ALTER COLUMN id type INTEGER;


/*
insert into "user" (name, surname, phone, email) VALUES
  ('Nadiia', 'Konon', '12', 'djfs@gm'),
  ('Svitlana', 'Konon', '1225', 'djfs@gm'),
  ('Anna', 'Konon', '12765756', 'djfs@g'),
  ('Sergiy', 'Konon', '134462', 'djfs');
*/

--select * from "user";


CREATE TABLE Country(
  id Serial PRIMARY KEY,
  name varchar(50) not null,
  unicode varchar(2) not null
);

CREATE TABLE city(
  id Serial PRIMARY KEY,
  name varchar(70) not null,
  postal_code varchar(10),
  country_id integer,
  CONSTRAINT country_foreigh_key FOREIGN KEY (country_id) REFERENCES Country(id)

);
