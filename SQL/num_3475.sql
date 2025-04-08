-- https://leetcode.com/problems/dna-pattern-recognition/description/?envType=problem-list-v2&envId=database
-- Medium

SELECT *,
COUNT(IF(dna_sequence LIKE 'ATG%', 1, NULL)) 'has_start',
COUNT(CASE
        WHEN dna_sequence LIKE '%TAA' OR dna_sequence LIKE '%TAG' OR dna_sequence LIKE '%TGA' THEN 1
        ELSE NULL
    END) as 'has_stop',
COUNT(IF(dna_sequence LIKE '%ATAT%', 1, NULL)) as 'has_atat',
COUNT(IF(dna_sequence REGEXP 'G{3,}', 1, NULL)) as 'has_ggg'
FROM Samples
GROUP BY sample_id