--
-- user
--

CREATE USER 'utente'@'%' identified by 'password';

GRANT ALL PRIVILEGES ON *.* TO 'utente';

FLUSH PRIVILEGES;

--
-- Data table
--
CREATE TABLE data (
  id int NOT NULL AUTO_INCREMENT,
  content varchar(1024) NOT NULL,
  PRIMARY KEY (id)
);

