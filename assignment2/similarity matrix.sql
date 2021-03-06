/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP 1000 [docid]
      ,[term]
      ,[count]
  FROM [GE AA Course].[dbo].[reuters]

SELECT f.r_rows, f.rt_cols, f.doc_similarity
FROM (
	SELECT r.r_rows, rt.rt_cols, SUM(r.r_counts*rt.rt_counts) as doc_similarity
	FROM ( 
		-- D-transpose matrix
		(SELECT [GE AA Course].[dbo].[reuters].term as rt_rows, [GE AA Course].[dbo].[reuters].docid as rt_cols, [GE AA Course].[dbo].[reuters].count as rt_counts
		FROM [GE AA Course].[dbo].[reuters]) as rt
		-- D matrix
		inner join
		(SELECT [GE AA Course].[dbo].[reuters].docid as r_rows, [GE AA Course].[dbo].[reuters].term as r_cols, [GE AA Course].[dbo].[reuters].count as r_counts
		FROM [GE AA Course].[dbo].[reuters]) as r
		on r.r_cols = rt.rt_rows)
	GROUP BY r.r_rows, rt.rt_cols) as f
WHERE f.r_rows = '10080_txt_crude'
AND f.rt_cols = '17035_txt_earn'
	


