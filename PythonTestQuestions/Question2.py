import os
import pyodbc
#import xlrd

def question2(path,server,db) :  
    
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
INSERT INTO [dbo].[Attribution]
           ([ID]
           ,[Quarter]
           ,[Attributed_Flag]
           ,[Risk_Score]
           ,[File_Date])

SELECT  [ID], 1, [Attributed Q1],[Risk Q1],'"""+file_date+"""'
        FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0', 
   'Excel 12.0 Xml;Database="""+path+file_name+""";','SELECT * FROM [Sheet1$B4:M]' )
  where [Risk Increased Flag] = 'Yes'

  UNION ALL
SELECT  [ID], 2, [Attributed Q2],[Risk Q2],'"""+file_date+"""'
        FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0', 
   'Excel 12.0 Xml;Database="""+path+file_name+""";','SELECT * FROM [Sheet1$B4:M]' )
  where [Risk Increased Flag] = 'Yes'
  ORDER BY 1,2
"""            
            # Execute sql Query
            cursor.execute(query)             
            print 'QUERY:', query
          
    # Commit the transaction
    conn.commit()
    
    # Close the database connection
    conn.close()
    
if __name__ == '__main__':
    question2('F:\\PriviaData\\','OFFICE2\SQLEXPRESS1432','PatientDatabase')
    


 
