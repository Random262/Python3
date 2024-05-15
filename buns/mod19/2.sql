SELECT
    s.full_name AS student_name,
    AVG(ag.grade) AS average_grade
FROM
    students s
JOIN
    assignments_grades ag ON s.student_id = ag.student_id
GROUP BY
    s.full_name
ORDER BY
    average_grade DESC
LIMIT 10;