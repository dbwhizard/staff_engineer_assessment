USE PERSONDATABASE

/*********************
Hello! 

Please use the test data provided in the file 'PersonDatabase' to answer the following
questions. Please also import the dbo.Contracts flat file to a table for use. 

All answers should be written in SQL. 


/**********************

QUESTION 1

Create a patient matching stored procedure that accepts (first name, last name, dob and sex) as parameters and 
and calculates a match score from the Person table based on the parameters given. If the parameters do not match the existing 
data exactly, create a partial match check using the weights below to assign partial credit for each. Return PatientIDs and the
 calculated match score. Feel free to modify or create any objects necessary in PersonDatabase.  

FirstName 
	Full Credit = 1
	Partial Credit = .5

LastName 
	Full Credit = .8
	Partial Credit = .4

Dob 
	Full Credit = .75
	Partial Credit = .3

Sex 
	Full Credit = .6
	Partial Credit = .25


**********************/
/*
Notes:
All Create scripts for the new objects are commited to this repository and have self-explanatory names.
I decided that in order to work with the Person data is needs to be cleaned and parsed, so I created a table to store the cleaned data, 
which includes separate fields for first, last names and alias/nickname. I also included there two computed columns for doing the fuzzy 
match on the first and last names, using well known metaphone algorythm.

I wrote the required sp, where I assume that the output score is the sum of the individual scores. My approcah is the first to find 
one or multiple table rows based on the fuzzy match (metaphones of the first and last names, Year-Month of DOB and variations 
of the Sex/Gender/Title descriptions, then I look at the degree of the match byevery field and assign corresponding individual scores.
*/



/**********************

QUESTION 2

Write script to load the dbo.Dates table with all applicable data elements for dates 
between 1/1/2010 and 500 days past the current date.


**********************/
/*
Most important point here is to decide how to create a necessary loop to polate the required number of the table rows without using
cursor and explicit loops. My solution uses system tables (it is not my original idea, credit goes to somebody else).

I commited the SQL Script 
*/

/**********************

QUESTION 3

Please import the data from the flat file dbo.Contracts.txt to a table to complete this question. 

Using the data in dbo.Contracts, create a query that returns 

	(PersonID, AttributionStartDate, AttributionEndDate) 

The data should be structured so that rows with contiguous ranges are merged into a single row. Rows that contain a 
break in time of 1 day or more should be entered as a new record in the output. Restarting a row for a new 
month or year is not necessary.

Use the dbo.Dates table if helpful.

**********************/
/*
I use two step process here to make it more readable and more manageable. First step creates a sequence of dates for each Person when 
they had attribution. The second step generates continous data ranges based on the above. I used CTE (Common Table Expressions) for the 2nd step as it
is the best approach to analyse and group set of rows. The resulting SQL Script is commited in this repository under the name AttributionIntervals.
