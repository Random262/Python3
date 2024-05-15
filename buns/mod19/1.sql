SELECT
    t.full_name AS teacher_name,
    AVG(ag.grade) AS average_grade
FROM
    teachers t
JOIN
    assignments a ON t.teacher_id = a.teacher_id
JOIN
    assignments_grades ag ON a.assisgnment_id = ag.assisgnment_id
GROUP BY
    t.full_name
ORDER BY
    average_grade
LIMIT 1;
