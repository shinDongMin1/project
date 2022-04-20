/*
drop table advisor
delete from advisor
*/
/*
1.
select name, tot_cred
from student
where dept_name = 'Physics'
2.
select title, credits
from course
where dept_name = 'Physics' and credits >= 3
3.
select name, salary
from instructor, department
where instructor.dept_name = department.dept_name and department.budget >= 100000
where instructor.dept_name = department.dept_name and budget >= 100000
4.
select name, salary
from instructor, teaches
where instructor.ID = teaches.ID and teaches.year = 2009 and teaches.semester = 'Fall'
where instructor.ID = teaches.ID and year = 2009 and semester = 'Fall'
5.
select student.name
from instructor, advisor, student
where instructor.dept_name = 'Physics' and instructor.ID = advisor.i_ID and student.ID = advisor.s_ID
*/

select distinct s1.ID, s1.name
from student s1, student s2 
where s1.tot_cred > s2.tot_cred and s2.dept_name = 'Comp. Sci.'

select distinct s1.dept_name, COUNT(distinct s1.ID)
from student s1, student s2
where s1.tot_cred > s2.tot_cred and s1.dept_name != 'Comp. Sci.' and s2.dept_name = 'Comp. Sci.' 
group by s1.dept_name
order by s1.dept_name

select *
from student
where dept_name = 'Accounting' and name like 'CH%'

select dept_name, budget
from department
where budget between 600000 and 800000
order by budget desc

(select ID from teaches where year = '2006' and semester = 'Spring')
except
(select ID from teaches where year = '2006' and semester = 'Fall')

update instructor
set salary = null
where dept_name = 'Pol. Sci.' or dept_name = 'Comp. Sci.'

select dept_name, count(*) cnt_instructor
from instructor
where salary is null
group by dept_name
order by dept_name

select year, semester, COUNT(distinct ID) cnt_student
from takes 
where grade != 'F' and grade is not null
group by year, semester
order by year, semester

select instructor.dept_name, count(distinct student.ID) cnt_student
from instructor, advisor, student
where student.ID = advisor.s_ID and advisor.i_ID = instructor.ID
group by instructor.dept_name
order by instructor.dept_name

select instructor.ID, count(distinct student.ID) cnt_student
from instructor, advisor, student
where student.ID = advisor.s_ID and advisor.i_ID = instructor.ID
group by instructor.ID
having count(distinct student.ID) >= 50
order by instructor.ID


select section.year, building, room_number, count(distinct student.ID) cnt_student
from student, takes, section
where student.ID = takes.ID and takes.course_id = section.course_id
group by section.year, building, room_number
order by section.year, building, room_number



select distinct student.ID
from student, takes, section
where student.ID = takes.ID and takes.course_id = section.course_id and building = 'Alumni' and room_number = '547' and takes.sec_id = section.sec_id and section.year = '2001'