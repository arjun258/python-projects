 select Title,Price from MOV where Price>20 order by Price;
 select * from MOV order by Qty desc;

 select No,Title,Price as 'Current Value',QTY * Price * 1.15 as 'Replacement Value' from MOV;