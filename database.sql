CREATE DATABASE payments;
USE payments;

CREATE TABLE creditcard
(
    id INT NOT NULL AUTO_INCREMENT,
    exp_date DATE NOT NULL,
    holder VARCHAR(100) NOT NULL,
    cc_number VARBINARY(200) NOT NULL,
    cvv INT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE user
(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(100) NOT NULL,
    passwrd VARCHAR(80) NOT NULL,
    PRIMARY KEY(id)
);