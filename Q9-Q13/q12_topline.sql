WITH CTE1 AS 
(
	SELECT mr.mailing_recipient_id, mr.mailing_id, mr.cons_id, c.gender, c.age_id
	FROM tradewater.mailing_recipient mr INNER JOIN tradewater.cons c ON mr.cons_id = c.cons_id 
),
CTE2 AS (
	SELECT CTE1.mailing_recipient_id, CTE1.mailing_id, CTE1.cons_id, CTE1.gender, CTE1.age_id, m.mailing_name 
	FROM CTE1 INNER JOIN tradewater.mailing m ON CTE1.mailing_id = m.mailing_id 
),
CTE3 AS (
	SELECT CTE2.mailing_recipient_id, CTE2.mailing_id, CTE2.cons_id, CTE2.gender, CTE2.age_id, CTE2.mailing_name, ca.cons_action_id 
	FROM CTE2 INNER JOIN tradewater.cons_action ca ON CTE2.cons_id = ca.cons_id 
),
CTE4 AS(
	SELECT CTE3.mailing_recipient_id, CTE3.mailing_id, CTE3.cons_id, CTE3.gender, CTE3.age_id, CTE3.mailing_name, CTE3.cons_action_id, mrc.mailing_recipient_click_id, mrc.mailing_recipient_click_type_id  
	FROM CTE3 INNER JOIN tradewater.mailing_recipient_click mrc ON CTE3.mailing_recipient_id = mrc.mailing_recipient_id 
),
Recipient_Count AS (
	SELECT CTE2.age_id, COUNT(CTE2.mailing_recipient_id) AS recipient_count
	FROM CTE2
	GROUP BY CTE2.age_id 
),
Opens_count AS (
	SELECT COUNT(cr.mailing_recipient_id) AS opens_count
	FROM tradewater.mailing_recipient_click cr INNER JOIN tradewater.mailing_recipient mr2 ON cr.mailing_recipient_id = mr2.mailing_recipient_id
	WHERE cr.mailing_recipient_click_type_id = 2
),
Click_count AS (
	SELECT COUNT(cr.mailing_recipient_id) AS click_count
	FROM tradewater.mailing_recipient_click cr INNER JOIN tradewater.mailing_recipient mr2 ON cr.mailing_recipient_id = mr2.mailing_recipient_id
	WHERE cr.mailing_recipient_click_type_id = 1
),
Opens_per_recipient AS (
	SELECT CTE2.age_id , COUNT(cr.mailing_recipient_id) AS opens_per_recipient
	FROM CTE2 INNER JOIN tradewater.mailing_recipient_click cr ON CTE2.mailing_recipient_id = cr.mailing_recipient_id 
	WHERE cr.mailing_recipient_click_type_id = 2
	GROUP BY CTE2.age_id  
),
Clicks_per_recipient AS (
	SELECT CTE2.age_id, COUNT(cr.mailing_recipient_id) AS clicks_per_recipient
	FROM CTE2 INNER JOIN tradewater.mailing_recipient_click cr ON CTE2.mailing_recipient_id = cr.mailing_recipient_id 
	WHERE cr.mailing_recipient_click_type_id = 1
	GROUP BY CTE2.age_id 
),
Number_of_actions AS (
	SELECT COUNT(CTE3.cons_action_id) AS number_of_actions
	FROM CTE3
),
Actions_per_recipient AS (
	SELECT CTE3.age_id , COUNT(CTE3.cons_action_id) AS actions_per_recipient
	FROM CTE3
	GROUP BY CTE3.age_id 
),
Combined_recipient AS(
	SELECT rc.age_id, recipient_count, opens_per_recipient, clicks_per_recipient, actions_per_recipient
	From Recipient_Count rc 
		INNER JOIN Opens_per_recipient opr 
			ON rc.age_id = opr.age_id
		INNER JOIN Clicks_per_recipient cpr
			ON cpr.age_id = opr.age_id
		INNER JOIN Actions_per_recipient napr
			ON napr.age_id = cpr.age_id
)
SELECT
	CASE 
		WHEN cr.age_id = 0 THEN '18-35'
		WHEN cr.age_id = 1 THEN '36-60'
		WHEN cr.age_id = 2 THEN '60+'
		ELSE NULL
	END AS age_group, 
	cr.recipient_count, 
	cr.opens_per_recipient, 
	oc.opens_count, 
	cr.clicks_per_recipient, 
	cc.click_count, 
	cr.actions_per_recipient, 
	na.number_of_actions
FROM Combined_recipient cr, Opens_count oc, Click_count cc, Number_of_actions na ;