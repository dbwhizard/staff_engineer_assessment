import os
import pyodbc
import pandas as pd

def question2(path,server,db) :  
    
    #server = 'OFFICE2\SQLEXPRESS1432'
    #db = 'PatientDatabase'
    #path='F:\\PriviaData\\'
                        
    
    # create Connection and Cursor objects
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes')
    conn.autocommit = True
    cursor = conn.cursor()


    # iterate thru folder  
    for file_name in os.listdir(path):
        if file_name.endswith(".xlsx"):            
 #          print "FILE", file_name
            length=len(file_name)
            file_date_mmddyy=file_name[length-11:length-5]
            file_date='20'+file_date_mmddyy[4:6]+'-'+file_date_mmddyy[0:2]+'-'+file_date_mmddyy[2:4]
            attribution_sheet1 = pd.read_excel(path+file_name, sheet_name=0,header=None,usecols="B,I:M",skiprows=4,converters={0:str,1:str,2:str,3:str,4:str,5:str})
         #  Give columns names to avoid relying on the spreadsheet headers being alway the same 
            attribution_sheet1.columns = ['ID','ATTRIBUTED_Q1','ATTRIBUTED_Q2','RISK_Q1','RISK_Q2','RISK_INCREASED_FLAG']
            
            for row in attribution_sheet1.itertuples():
   
                # use data only if risk_increased_flag is Yes
                 if row.RISK_INCREASED_FLAG == 'Yes': 
                  query = """
                  INSERT INTO [dbo].[Attribution]
                  ([ID]
                  ,[Quarter]
                  ,[Attributed_Flag]
                  ,[Risk_Score]
                  ,[File_Date]) VALUES ( '"""  
                  query = "USE " + db + query
           # will run 2 inserts per dataframe row  
              
                  query1 = query+ row.ID+ "','1','" +row.ATTRIBUTED_Q1+ "','"+row.RISK_Q1+ "','" +file_date+"');"
                # Execute 1st Insert Query
                  cursor.execute(query1)
                  
                  query2 = query+ row.ID+ "','2','" +row.ATTRIBUTED_Q2+ "','"+row.RISK_Q2+ "','" +file_date+"');"
                # Execute 2nd Insert Query
                  cursor.execute(query2)             
         
    # Commit the transaction
    conn.commit()
    
    # Close the database connection
    conn.close()
    
if __name__ == '__main__':
    question2('E:\\','PENNS-MIS-LB\SQLEXPRESS','PatientDatabase')
    


 