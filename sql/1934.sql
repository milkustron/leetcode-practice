SELECT user_id, 
IFNULL(ROUND(SUM(IF(action = 'confirmed', 1, 0))/COUNT(action),2), 0) AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations USING(user_id)
GROUP BY user_id