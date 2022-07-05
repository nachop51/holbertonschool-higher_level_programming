-- Script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM hbtn_0c_0.temperatures GROUP BY city ORDER BY avg_temp DESC;
