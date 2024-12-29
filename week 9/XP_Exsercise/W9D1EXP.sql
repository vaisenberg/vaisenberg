SELECT 
    m.medal_name AS medal_type,
    (
        SELECT AVG(gc.age)
        FROM olympics.games_competitor gc
        WHERE gc.id IN (
            SELECT ce.competitor_id
            FROM olympics.competitor_event ce
            WHERE ce.medal_id = m.id
        )
    ) AS average_age
FROM 
    olympics.medal m
WHERE 
    m.medal_name IS NOT NULL;
----------------------------------

-- TASK 2

SELECT 
    (SELECT region_name 
     FROM olympics.noc_region r 
     WHERE r.id = pr.region_id) AS region,
    COUNT(DISTINCT pr.person_id) AS unique_competitors
FROM 
    olympics.person_region pr
WHERE 
    pr.person_id IN (
        SELECT ce.competitor_id
        FROM olympics.competitor_event ce
        GROUP BY ce.competitor_id
        HAVING COUNT(DISTINCT ce.event_id) > 3
    )
GROUP BY 
    pr.region_id
ORDER BY 
    unique_competitors DESC
LIMIT 5;
----------------------------------------
-- Task 3

CREATE TEMP TABLE competitor_medals AS
SELECT 
    ce.competitor_id,
    COUNT(ce.medal_id) AS total_medals
FROM 
    olympics.competitor_event ce
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    ce.competitor_id
HAVING 
    COUNT(ce.medal_id) > 2;

SELECT * FROM competitor_medals;

---------------------------------------

--Task 4
CREATE TEMP TABLE competitor_analysis AS
SELECT 
    ce.competitor_id,
    COUNT(ce.medal_id) AS total_medals
FROM 
    olympics.competitor_event ce
GROUP BY 
    ce.competitor_id;

DELETE FROM competitor_analysis
WHERE competitor_id IN (
    SELECT competitor_id
    FROM competitor_analysis
    WHERE total_medals = 0
);

SELECT * FROM competitor_analysis;
-------------------------------------------------
-- Exercise 2: Advanced Data Manipulation and Optimization
-- Task 1
UPDATE olympics.person
SET height = (
    SELECT AVG(p2.height)
    FROM olympics.person p2
    WHERE p2.id IN (
        SELECT pr2.person_id
        FROM olympics.person_region pr2
        WHERE pr2.region_id = (
            SELECT pr.region_id
            FROM olympics.person_region pr
            WHERE pr.person_id = olympics.person.id
        )
    )
)
WHERE height IS NULL; 
---------------------------------------------------------
-- Task 2

CREATE TEMP TABLE multi_event_competitors2 AS
SELECT 
    gc.person_id AS competitor_id,
    gc.games_id,
    (
        SELECT COUNT(ce.event_id)
        FROM olympics.competitor_event ce
        WHERE ce.competitor_id = gc.person_id
          AND ce.event_id IN (
              SELECT DISTINCT event_id
              FROM olympics.competitor_event
              WHERE competitor_id = gc.person_id
          )
    ) AS total_events
FROM 
    olympics.games_competitor gc
WHERE 
    gc.person_id IN (
        SELECT ce.competitor_id
        FROM olympics.competitor_event ce
        GROUP BY ce.competitor_id, ce.event_id
        HAVING COUNT(DISTINCT ce.event_id) > 1
    );
SELECT *
FROM multi_event_competitors2;

------------------------------------------
-- Task3
SELECT 
    pr.region_id,
    pr.person_id,
    COUNT(ce.medal_id) AS medals_per_competitor
FROM 
    olympics.person_region pr
LEFT JOIN 
    olympics.competitor_event ce ON pr.person_id = ce.competitor_id
WHERE 
    ce.medal_id IS NOT NULL
GROUP BY 
    pr.region_id, pr.person_id

---------------------------------------------------
-- Task 4
-- Step 1: Create a temporary table for analysis
CREATE TEMP TABLE competitor_analysis4 AS
SELECT 
    ce.competitor_id,
    COUNT(ce.medal_id) AS total_medals
FROM 
    olympics.competitor_event ce
GROUP BY 
    ce.competitor_id;

-- Step 2: Delete competitors with zero medals
DELETE FROM competitor_analysis4
WHERE competitor_id IN (
    SELECT competitor_id
    FROM competitor_analysis
    WHERE total_medals = 0
);

-- Step 3: Verify the remaining records
SELECT *
FROM competitor_analysis4;


