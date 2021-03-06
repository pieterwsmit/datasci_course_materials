/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [docid]
      ,[term]
      ,[count]
  FROM [GE AA Course].[dbo].[reuters]
  
/*
CREATE VIEW query_document as 
SELECT * FROM reuters
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
*/

SELECT f.r_rows, f.rt_cols, f.doc_similarity
FROM (
	SELECT r.r_rows, rt.rt_cols, SUM(r.r_counts*rt.rt_counts) as doc_similarity
	FROM ( 
		-- D-transpose matrix
		(SELECT dbo.query_document.term as rt_rows, dbo.query_document.docid as rt_cols, dbo.query_document.count as rt_counts
		FROM dbo.query_document) as rt
		-- D matrix
		inner join
		(SELECT dbo.query_document.docid as r_rows, dbo.query_document.term as r_cols, dbo.query_document.count as r_counts
		FROM dbo.query_document) as r
		on r.r_cols = rt.rt_rows)
	GROUP BY r.r_rows, rt.rt_cols) as f
WHERE f.r_rows = 'q'
--AND f.rt_cols = '17035_txt_earn'
order by f.doc_similarity desc	
	
