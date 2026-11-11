CREATE DATABASE gym_db;
USE gym_db;
CREATE TABLE member (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    place VARCHAR(100),
    mobile VARCHAR(15) UNIQUE,
    plan ENUM(
        "1 Month",
        "2 Month",
        "3 Month",
        "6 Month",
        "8 Month",
        "1 Year"
    ),
    fee INT,
    join_date DATE
);

DESCRIBE member;