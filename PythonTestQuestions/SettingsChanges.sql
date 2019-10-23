p_configure 'show advanced options', 1
 RECONFIGURE
 GO

 sp_configure 'Ad Hoc Distributed Queries', 1
 RECONFIGURE
 GO


 EXEC master.[sys].[sp_MSset_oledb_prop] N'Microsoft.ACE.OLEDB.12.0', N'AllowInProcess', 1
 
  
 
 
/* 
http://www.aspsnippets.com/Articles/The-OLE-DB-provider-Microsoft.Ace.OLEDB.12.0-for-linked-server-null.aspx
 
 This solves the issue. For some reason SQL Server does not like the default MSSQLSERVER account. Switching it to a local user account resolves the issue.
*/
