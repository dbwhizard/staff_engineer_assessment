USE [PatientDatabase]
GO

/****** Object:  Table [dbo].[Demographics]    Script Date: 10/22/2019 11:03:59 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON
GO

CREATE TABLE [dbo].[Demographics](
Provider_Group nvarchar(255),
File_Date Date,
	[ID] [nvarchar](255) NULL,
	[First Name] [nvarchar](255) NULL,
	[Middle Name] [nvarchar](255) NULL,
	[Last Name] [nvarchar](255) NULL,
	[DOB] [datetime] NULL,
	[Sex] [char](1) NULL,
	[Favorite Color] [nvarchar](255) NULL,
) ON [PRIMARY]

GO

SET ANSI_PADDING OFF
GO
