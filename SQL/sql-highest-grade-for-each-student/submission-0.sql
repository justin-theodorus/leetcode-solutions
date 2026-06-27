-- Write your query below
SELECT er.student_id, exam_id, score
FROM exam_results er
JOIN (
    SELECT student_id, MAX(score) AS max_score
    FROM exam_results
    GROUP BY student_id
) tmp ON er.student_id = tmp.student_id
WHERE score = max_score AND exam_id = (
    SELECT MIN(exam_id) AS min_exam_id
    FROM exam_results
    WHERE student_id = er.student_id AND
    score = max_score
)
ORDER BY er.student_id;


