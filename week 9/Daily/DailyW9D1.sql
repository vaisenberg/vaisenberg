--  Exercise 1: Detailed Medal Analysis

-- Task 1
CREATE TEMP TABLE competitors_season_medals AS
SELECT 
    pr.person_id AS competitor_id,
    SUM(CASE WHEN (SELECT g.season FROM olympics.games g WHERE g.id = gc.games_id) = 'Summer' THEN 1 ELSE 0 END) AS summer_medals,
    SUM(CASE WHEN (SELECT g.season FROM olympics.games g WHERE g.id = gc.games_id) = 'Winter' THEN 1 ELSE 0 END) AS winter_medals
FROM 
    olympics.person_region pr
JOIN 
    olympics.games_competitor gc ON pr.person_id = gc.person_id
WHERE 
    pr.person_id IN (
        SELECT ce.competitor_id
        FROM olympics.competitor_event ce
        WHERE ce.medal_id IS NOT NULL
    )
GROUP BY 
    pr.person_id
HAVING 
    SUM(CASE WHEN (SELECT g.season FROM olympics.games g WHERE g.id = gc.games_id) = 'Summer' THEN 1 ELSE 0 END) > 0
    AND SUM(CASE WHEN (SELECT g.season FROM olympics.games g WHERE g.id = gc.games_id) = 'Winter' THEN 1 ELSE 0 END) > 0;


SELECT *
FROM competitors_season_medals;
---------------------------------------------------------

-- Task 2
CREATE TEMP TABLE two_sport_medalists AS
SELECT 
    ce.competitor_id,
    COUNT(DISTINCT e.sport_id) AS sports_count,
    COUNT(ce.medal_id) AS total_medals
FROM 
    olympics.competitor_event ce
JOIN 
    olympics.event e ON ce.event_id = e.id
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    ce.competitor_id
HAVING 
    COUNT(DISTINCT e.sport_id) = 2;

SELECT *
FROM (
    SELECT 
        competitor_id,
        total_medals
    FROM 
        two_sport_medalists
    ORDER BY 
        total_medals DESC
    LIMIT 3
) AS top_three_medalists;

SELECT * FROM two_sport_medalists;
------------------------------------------

--  Exercise 2: Region and Competitor Performance
-- Task 1
CREATE TEMP TABLE competitor_event_medals AS
SELECT 
    ce.competitor_id,
    ce.event_id,
    COUNT(ce.medal_id) AS medals_in_event
FROM 
    olympics.competitor_event ce
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    ce.competitor_id, ce.event_id;
CREATE TEMP TABLE max_medals_per_competitor AS
SELECT 
    competitor_id,
    MAX(medals_in_event) AS max_medals
FROM 
    competitor_event_medals
GROUP BY 
    competitor_id;
SELECT 
    r.region_name,
    SUM(mmpc.max_medals) AS total_medals
FROM 
    olympics.person_region pr
JOIN 
    max_medals_per_competitor mmpc ON pr.person_id = mmpc.competitor_id
JOIN 
    olympics.noc_region r ON pr.region_id = r.id
GROUP BY 
    r.region_name
ORDER BY 
    total_medals DESC
LIMIT 5;
-------------------------------------------
-- Task 2
CREATE TEMP TABLE no_medals_three_games AS
SELECT 
    p.id AS competitor_id,
    p.full_name,
    COUNT(DISTINCT gc.games_id) AS games_participated
FROM 
    olympics.person p
JOIN 
    olympics.games_competitor gc ON p.id = gc.person_id
WHERE 
    p.id NOT IN (
        SELECT DISTINCT ce.competitor_id
        FROM olympics.competitor_event ce
        WHERE ce.medal_id IS NOT NULL
    )
GROUP BY 
    p.id, p.full_name
HAVING 
    COUNT(DISTINCT gc.games_id) > 3;

SELECT * FROM no_medals_three_games;

 


