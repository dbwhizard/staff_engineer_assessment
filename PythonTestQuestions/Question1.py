import os
import pyodbc
#import xlrd

def question1(path,server,db) :  
    
    #server = 'OFFICE2\SQLEXPRESS1432'
    #db = 'PatientDatabase'
    #path='F:\\PriviaData\\'
    
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
    conn.autocommit = True
    cursor = conn.cursor()


    # iterate thru folder  
    for file_name in os.listdir(path):
        if file_name.endswith(".xlsx"):
            
            #print "FILE:", file_name
            
            length=len(file_name)
            file_date_mmddyy=file_name[length-11:length-5]
            file_date='20'+file_date_mmddyy[4:6]+'-'+file_date_mmddyy[0:2]+'-'+file_date_mmddyy[2:4]
            provider_group=file_name[0:length-11]
            print file_date, "-",provider_group
            
            
            # create Connection and Cursor objects            
            query = """
USE PatientDatabase
INSERT INTO [dbo].[Demographics]
           ([Provider_Group]
           ,[File_Date]
           ,[ID]
           ,[First Name]
           ,[Middle Name]
           ,[Last Name]
           ,[DOB]
           ,[Sex]
           ,[Favorite Color])

SELECT '""" +provider_group+ "','" +file_date+ """',
LTRIM(RTRIM([ID])),	LTRIM(RTRIM([First Name])),	SUBSTRING (LTRIM(RTRIM([Middle Name])),1,1) Middle_Name,	LTRIM(RTRIM([Last Name])),	LTRIM(RTRIM([DOB(1)])),	
CASE WHEN LTRIM(RTRIM([Sex]))=0 THEN 'M' ELSE 'F' END Sex
,	LTRIM(RTRIM([Favorite Color]))  
FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0', 
   'Excel 12.0 Xml;Database=""" +path+ file_name + """;','SELECT * FROM [Sheet1$B4:H]' );
"""            
            # Execute sql Query
            cursor.execute(query)             
            #print 'QUERY:', query
          
    # Commit the transaction
    conn.commit()
    
    # Close the database connection
    conn.close()
    
if __name__ == '__main__':
    question1('F:\\PriviaData\\','OFFICE2\SQLEXPRESS1432','PatientDatabase')
    


 
