-- Q1 --
SELECT COUNT(*)
FROM TestTable;

-- Q2 --
SELECT Firstname, Lastname
FROM TestTable;

-- Q3 --
SELECT DISTINCT(Firstname), COUNT(Firstname)
FROM TestTable;

-- Q4 --
SELECT P.Firstname, 
    P.Lastname,
    PA.Address1, 
    PA.Address2, 
    PA.City, 
    PA.State, 
    PA.Zip
FROM Person AS P INNER JOIN PersonAddress AS PA ON P.PersonID = PA.PersonID;

-- Q5 -- 
SELECT P.Firstname, 
    P.Lastname, 
    CASE
        WHEN  PA.Address1 IS NULL THEN 'PLACEHOLDER DATA'
        ELSE  PA.Address1 
    END,
    CASE
        WHEN  PA.Address2 IS NULL THEN 'PLACEHOLDER DATA'
        ELSE  PA.Address2 
    END,
    CASE
        WHEN  PA.City IS NULL THEN 'PLACEHOLDER DATA'
        ELSE  PA.City 
    END,
    CASE
        WHEN  PA.State IS NULL THEN 'PLACEHOLDER DATA'
        ELSE  PA.State 
    END,
    CASE
        WHEN  PA.Zip IS NULL THEN 'PLACEHOLDER DATA'
        ELSE  PA.Zip 
    END

FROM Person AS P INNER JOIN PersonAddress AS PA ON P.PersonID = PA.PersonID;

-- Q6 -- 

WITH Person_Info_Tmp AS
(
    SELECT P.Firstname, 
        P.Lastname, 
        CASE
            WHEN  PA.Address1 IS NULL THEN 'PLACEHOLDER DATA'
            ELSE  PA.Address1 
        END,
        CASE
            WHEN  PA.Address2 IS NULL THEN 'PLACEHOLDER DATA'
            ELSE  PA.Address2 
        END,
        CASE
            WHEN  PA.City IS NULL THEN 'PLACEHOLDER DATA'
            ELSE  PA.City 
        END,
        CASE
            WHEN  PA.State IS NULL THEN 'PLACEHOLDER DATA'
            ELSE  PA.State 
        END,
        CASE
            WHEN  PA.Zip IS NULL THEN 'PLACEHOLDER DATA'
            ELSE  PA.Zip 
        END

    FROM Person AS P INNER JOIN PersonAddress AS PA ON P.PersonID = PA.PersonID
)
SELECT * FROM Person_Info_Tmp ;