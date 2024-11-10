SELECT request_at AS Day, 
ROUND(SUM(IF(status LIKE 'cancelled%' AND driver.banned = 'No' AND client.banned = 'No', 1, 0))/SUM(IF(driver.banned = 'No' AND client.banned = 'No', 1, 0)),2) AS `Cancellation Rate`
FROM Trips
LEFT JOIN Users AS driver ON Trips.driver_id = driver.users_id 
LEFT JOIN Users AS client ON Trips.client_id = client.users_id 
WHERE request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY request_at
HAVING `Cancellation Rate` IS NOT NULL