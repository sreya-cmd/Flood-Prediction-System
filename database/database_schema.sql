CREATE TABLE User (
    user_id INT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100),
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE WeatherData (
    data_id INT PRIMARY KEY,
    user_id INT,
    annual_rainfall FLOAT,
    cloud_visibility FLOAT,
    seasonal_rainfall FLOAT,
    temperature FLOAT,
    humidity FLOAT,
    FOREIGN KEY(user_id) REFERENCES User(user_id)
);

CREATE TABLE MLModel (
    model_id INT PRIMARY KEY,
    model_name VARCHAR(100),
    algorithm VARCHAR(100),
    accuracy FLOAT,
    model_file VARCHAR(200)
);

CREATE TABLE Prediction (
    prediction_id INT PRIMARY KEY,
    data_id INT,
    model_id INT,
    prediction_result VARCHAR(20),
    flood_probability FLOAT,
    prediction_date DATE,
    FOREIGN KEY(data_id) REFERENCES WeatherData(data_id),
    FOREIGN KEY(model_id) REFERENCES MLModel(model_id)
);