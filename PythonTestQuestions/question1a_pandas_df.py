import os
import pyodbc
import pandas as pd

def question1(path,server,db) :  
    
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

            length=len(file_name)
            file_date_mmddyy=file_name[length-11:length-5]
            file_date='20'+file_date_mmddyy[4:6]+'-'+file_date_mmddyy[0:2]+'-'+file_date_mmddyy[2:4]
            provider_group=file_name[0:length-11]
            attribution_sheet1 = pd.read_excel(path+file_name, sheet_name=0,header=None,usecols="B:H", skiprows=4,converters={0:str,1:str,2:str,3:str,4:str,5:str,6:str})
            attribution_sheet1.columns = ['ID','FIRST_NAME','MIDDLE_NAME','LAST_NAME','DOB','SEX','FAVORITE_COLOR']

            for row in attribution_sheet1.itertuples():
            # shorten middle name - Q#1d
                if pd.isnull(row.MIDDLE_NAME): 
                    middle_initial=" "
                else:
                    middle_initial=row.MIDDLE_NAME[0:1]
                    # Convert the Sex values
                if row.SEX == "0":
                    converted_sex = "M"
                elif row.SEX == "1":
        	    	converted_sex = "F"
                else:  
        	    	converted_sex = "U"
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
               ,[Favorite Color]) VALUES ( '"""  
                query = query + provider_group+ "','" +file_date+ "','"+row.ID+ "','" +row.FIRST_NAME+ "','" +middle_initial+ "','" +row.LAST_NAME+ "','" +row.DOB[0:9]+ "','" +converted_sex+"','"+row.FAVORITE_COLOR+"');"
                # Execute sql Query
                cursor.execute(query)             
         
    # Commit the transaction
    conn.commit()
    
    # Close the database connection
    conn.close()
    
if __name__ == '__main__':
    question1('E:\\','PENNS-MIS-LB\SQLEXPRESS','PatientDatabase')
    


 