with 
nums as 
    (select level num from dual connect by level<=1000),
allnums as
    (select num, (select count(mod(n1.num,n2.num)) from nums n2 where n2.num<=round(n1.num/2) and   mod(n1.num,n2.num)=0) c from nums n1)
select num from allnums where c=1;  


with 
nums as 
    (select level num from dual connect by level<=1000),
allnums as
    (select num, (select count(mod(n1.num,n2.num)) from nums n2 where n2.num<=round(n1.num/2) and   mod(n1.num,n2.num)=0) c from nums n1 where n1.num>1)
select LISTAGG(num, ',') within group (order by num) from allnums where c=1;
