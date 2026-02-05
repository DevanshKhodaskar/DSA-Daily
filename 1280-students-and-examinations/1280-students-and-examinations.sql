SELECT 
    crs.student_id,
    crs.student_name,crs.subject_name,
    COUNT(e.student_id) AS attended_exams
FROM
    (SELECT s.student_id, s.student_name, sub.subject_name
     FROM Students s
     CROSS JOIN Subjects sub) crs
LEFT JOIN Examinations e
    ON e.student_id = crs.student_id
   AND e.subject_name = crs.subject_name
GROUP BY 
    crs.student_id, crs.student_name, crs.subject_name
ORDER BY 
    crs.student_id, crs.subject_name;
