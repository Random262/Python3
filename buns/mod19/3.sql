SELECT
    s.full_name AS student_name
FROM
    students s
JOIN
    students_groups sg ON s.group_id = sg.group_id
JOIN
    assignments a ON sg.group_id = a.group_id
JOIN
    teachers t ON a.teacher_id = t.teacher_id
WHERE
    t.teacher_id = (
        SELECT
            a.teacher_id
        FROM
            assignments a
        JOIN
            assignments_grades ag ON a.assisgnment_id = ag.assisgnment_id
        GROUP BY
            a.teacher_id
        ORDER BY
            AVG(ag.grade) DESC
        LIMIT 1
    );
