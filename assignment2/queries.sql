#1
select count(*) from Frequency where docid = "10398_txt_earn";
#2
select count(term) from Frequency where docid = "10398_txt_earn" and count = 1;
#3
select count(term) from (select term from Frequency where docid = "10398_txt_earn" and count = 1 
                         UNION select term from Frequency where docid = "925_txt_trade" and count = 1);
#4
select count(term) from Frequency where term like 'parliament';
#5
select count(docid) from (select sum(count) as c1, docid from Frequency group by docid) where c1 > 300;
#6
select distinct count(docid) from (select docid from Frequency Where term = 'transaction' INTERSECT select docid from Frequency Where term = 'world');

#7 (Matrix multiplication with SQL) A[i,k] * B[k,j] = C[i,j]
select A.row_num,B.col_num,sum(A.value*B.value) from A,B WHERE A.col_num = B.row_num group by A.row_num, B.col_num;
#8 S = D*D'
select sum(A.count*B.count) from Frequency A, Frequency B WHERE A.term = B.term and A.docid = '10080_txt_crude' and B.docid = '17035_txt_earn';
#9
create view keyword as 
                        SELECT * FROM frequency
                        UNION
                        SELECT 'q' as docid, 'washington' as term, 1 as count 
                        UNION
                        SELECT 'q' as docid, 'taxes' as term, 1 as count
                        UNION 
                        SELECT 'q' as docid, 'treasury' as term, 1 as count
                        
select A.docid,sum(A.count*B.count)as score from keyword A, keyword B WHERE A.term = B.term and B.docid="q" Group By A.docid order by -score limit 10;