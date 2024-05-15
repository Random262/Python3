SELECT
    sg.group_id,
    COUNT(s.student_id) AS total_students,
    AVG(ag.grade) AS average_grade,
    COUNT(CASE WHEN ag.grade IS NULL THEN 1 END) AS not_submitted_count,
    COUNT(CASE WHEN ag.date > a.due_date THEN 1 END) AS overdue_count,
    COUNT(CASE WHEN ag.grade IS NOT NULL THEN 1 END) - COUNT(CASE WHEN ag.grade = 0 THEN 1 END) AS retry_count
FROM
    students_groups sg
LEFT JOIN
    students s ON sg.group_id = s.group_id
LEFT JOIN
    assignments_grades ag ON s.student_id = ag.student_id
LEFT JOIN
    assignments a ON ag.assisgnment_id = a.assisgnment_id
GROUP BY
    sg.group_id;