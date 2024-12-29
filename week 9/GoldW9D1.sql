-- Step 1: Identify competitors who won medals in individual events
CREATE TEMP TABLE individual_event_medals AS
SELECT DISTINCT ce.competitor_id
FROM olympics.competitor_event ce
JOIN olympics.event e ON ce.event_id = e.id
JOIN olympics.sport s ON e.sport_id = s.id
WHERE s.sport_name NOT LIKE '%Team%' -- Assuming 'Team' keyword differentiates individual events
  AND ce.medal_id IS NOT NULL;

-- Step 2: Identify competitors who won medals in team events
CREATE TEMP TABLE team_event_medals AS
SELECT DISTINCT ce.competitor_id
FROM olympics.competitor_event ce
JOIN olympics.event e ON ce.event_id = e.id
JOIN olympics.sport s ON e.sport_id = s.id
WHERE s.sport_name LIKE '%Team%' -- Assuming 'Team' keyword differentiates team events
  AND ce.medal_id IS NOT NULL;

-- Step 3: Identify competitors who have won medals in both individual and team events
CREATE TEMP TABLE both_event_medals AS
SELECT iem.competitor_id
FROM individual_event_medals iem
INTERSECT
SELECT tem.competitor_id
FROM team_event_medals tem;

-- Step 4: Retrieve details of these competitors
SELECT 
    p.id AS competitor_id,
    p.full_name
FROM olympics.person p
WHERE p.id IN (SELECT competitor_id FROM both_event_medals);


-------------------------------------------
-- Step 1: Create a temporary table for cumulative medal count per region
CREATE TEMP TABLE region_medal_counts AS
SELECT 
    pr.region_id,
    r.region_name,
    COUNT(ce.medal_id) AS total_medals
FROM 
    olympics.person_region pr
JOIN 
    olympics.competitor_event ce ON pr.person_id = ce.competitor_id
JOIN 
    olympics.noc_region r ON pr.region_id = r.id
WHERE 
    ce.medal_id IS NOT NULL -- Only count valid medals
GROUP BY 
    pr.region_id, r.region_name;

-- Step 2: Find the top 3 regions with the highest cumulative medal count
SELECT 
    region_name,
    total_medals
FROM 
    region_medal_counts
ORDER BY 
    total_medals DESC
LIMIT 3;
--------------------------------------------
-- Step 1: Create a temporary table for competitors meeting the conditions
CREATE TEMP TABLE gold_medalists_multiple_games AS
SELECT 
    gc.person_id AS competitor_id,
    COUNT(DISTINCT gc.games_id) AS games_participated,
    (SELECT COUNT(ce.medal_id)
     FROM olympics.competitor_event ce
     WHERE ce.competitor_id = gc.person_id
       AND ce.medal_id = (
           SELECT id
           FROM olympics.medal
           WHERE medal_name = 'Gold'
       )
    ) AS gold_medals_won
FROM 
    olympics.games_competitor gc
WHERE 
    gc.person_id IN (
        SELECT ce.competitor_id
        FROM olympics.competitor_event ce
        WHERE ce.medal_id = (
            SELECT id
            FROM olympics.medal
            WHERE medal_name = 'Gold'
        )
    )
GROUP BY 
    gc.person_id
HAVING 
    COUNT(DISTINCT gc.games_id) > 2;

-- Step 2: Retrieve and display the contents of the temporary table
SELECT *
FROM gold_medalists_multiple_games;
---------------------------------------------------------------------------
-- Step 1: Update weights for competitors who have won medals in multiple games
UPDATE olympics.person
SET weight = (
    SELECT AVG(p.weight)
    FROM olympics.person p
    WHERE p.id IN (
        SELECT DISTINCT ce.competitor_id
        FROM olympics.competitor_event ce
        WHERE ce.medal_id IS NOT NULL
    )
)
WHERE id IN (
    SELECT gc.person_id
    FROM olympics.games_competitor gc
    WHERE gc.person_id IN (
        SELECT ce.competitor_id
        FROM olympics.competitor_event ce
        WHERE ce.medal_id IS NOT NULL
        GROUP BY ce.competitor_id
        HAVING COUNT(DISTINCT ce.event_id) > 1
    )
);
------------------------------------------------

-- Step 1: Create a temporary table to store the number of events participated by each competitor
CREATE TEMP TABLE competitor_event_count AS
SELECT 
    gc.person_id AS competitor_id,
    COUNT(DISTINCT ce.event_id) AS events_participated,
    ARRAY_AGG(DISTINCT g.season) AS seasons_participated
FROM 
    olympics.games_competitor gc
JOIN 
    olympics.competitor_event ce ON gc.person_id = ce.competitor_id
JOIN 
    olympics.games g ON gc.games_id = g.id
GROUP BY 
    gc.person_id;

-- Step 2: Identify competitors who have participated in events across different seasons
CREATE TEMP TABLE multi_season_competitors AS
SELECT 
    competitor_id,
    events_participated,
    seasons_participated
FROM 
    competitor_event_count
WHERE 
    ARRAY_LENGTH(seasons_participated, 1) > 1;

-- Step 3: Display the details of these competitors
SELECT 
    p.id AS competitor_id,
    p.full_name,
    msc.events_participated,
    msc.seasons_participated
FROM 
    olympics.person p
JOIN 
    multi_season_competitors msc ON p.id = msc.competitor_id;
-----------------------------------------------------------------------

CREATE TEMP TABLE region_avg_height AS
SELECT 
    pr.region_id,
    r.region_name,
    AVG(p.height) AS avg_height_medal_winners
FROM 
    olympics.person_region pr
JOIN 
    olympics.person p ON pr.person_id = p.id
JOIN 
    olympics.competitor_event ce ON p.id = ce.competitor_id
JOIN 
    olympics.noc_region r ON pr.region_id = r.id
WHERE 
    ce.medal_id IS NOT NULL -- Only consider medal winners
GROUP BY 
    pr.region_id, r.region_name;

-- Step 2: Calculate the overall average height of all competitors
CREATE TEMP TABLE overall_avg_height AS
SELECT 
    AVG(height) AS avg_height_all_competitors
FROM 
    olympics.person;

-- Step 3: Compare the regional average heights with the overall average height
SELECT 
    rah.region_name,
    rah.avg_height_medal_winners,
    oah.avg_height_all_competitors,
    CASE 
        WHEN rah.avg_height_medal_winners > oah.avg_height_all_competitors THEN 'Above Average'
        WHEN rah.avg_height_medal_winners = oah.avg_height_all_competitors THEN 'Equal to Average'
        ELSE 'Below Average'
    END AS comparison
FROM 
    region_avg_height rah
CROSS JOIN 
    overall_avg_height oah;






