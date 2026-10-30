SELECT 
    e.left_operand AS left_operand,
    operator,
    e.right_operand AS right_operand,
    CASE
        WHEN e.operator = '>' AND l.value > r.value THEN 'true'
        WHEN e.operator = '<' AND l.value < r.value THEN 'true'
        WHEN e.operator = '=' AND l.value = r.value THEN 'true'
        ELSE 'false'
    END AS value
FROM expressions e
JOIN variables l ON l.name = e.left_operand
JOIN variables r ON r.name = e.right_operand;

