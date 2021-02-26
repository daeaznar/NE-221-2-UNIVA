    CREATE TABLE `school_flask`.`student` ( `id` INT NOT NULL AUTO_INCREMENT , `first_name` VARCHAR(45) NOT NULL , `last_name` VARCHAR(45) NOT NULL , `is_active` BOOLEAN NOT NULL DEFAULT TRUE , `create_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , `update_at` TIMESTAMP on update CURRENT_TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP , PRIMARY KEY (`id`)) ENGINE = InnoDB;


CREATE VIEW school_v AS 
SELECT
	school.id AS 'id',
    name AS 'name',
    description AS 'description',
    is_active as 'is_active',
    create_at AS 'create_at',
    update_at AS 'update_at',
    teacher_id AS 'teacher_id',
    teacher.first_name AS 'teacher_first_name',
    student_id AS 'student_id',
    student.first_name AS 'student_first_name'
FROM school
INNER JOIN teacher ON teacher.id=school.teacher_id
INNER JOIN student ON student.id = school.student_id