CREATE DATABASE chronic_disease_registry;
USE chronic_disease_registry;

CREATE TABLE Patient (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(1),
    phone VARCHAR(20) UNIQUE
);

CREATE TABLE Disease (
    disease_id INT PRIMARY KEY AUTO_INCREMENT,
    name CHAR(200) NOT NULL,
    description TEXT
);

CREATE TABLE Treatment (
    treatment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    disease_id INT,
    medication VARCHAR(300),
    start_date DATE NOT NULL,
    end_date DATE,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (disease_id) REFERENCES Disease(disease_id)
);

CREATE TABLE Doctor (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL ,
    specialization VARCHAR(100)
);

CREATE TABLE Appointment (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
);