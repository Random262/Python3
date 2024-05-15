SELECT
    group_id,
    AVG(overdue_count) AS average_overdue_count,
    MAX(overdue_count) AS max_overdue_count,
    MIN(overdue_count) AS min_overdue_count
FROM (
    SELECT
        sg.group_id,
        COUNT(*) AS overdue_count
    FROM
        students_groups sg
    JOIN
        students s ON sg.group_id = s.group_id
    JOIN
        assignments_grades ag ON s.student_id = ag.student_id
    JOIN
        assignments a ON ag.assisgnment_id = a.assisgnment_id
    WHERE
        ag.date > a.due_date
    GROUP BY
        sg.group_id
) AS subquery
GROUP BY
    group_id;
