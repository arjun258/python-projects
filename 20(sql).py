 select Name from Student where Stream != 'Medical';
select Name from Student where class in ('12B','12C','12A','12D') order by Stipend;
select Name from Student order by AvgMark desc;
 select Name,Stipend,Stream,Stipend*12 as 'yearly Stipend' from Student;
