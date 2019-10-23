USE [PatientDatabase]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Attribution](
	[ID] [nvarchar](255) NULL,
	[Quarter] [int] NULL,
	[Attributed_Flag] nvarchar(3) NULL,
	[Risk_Score] [float] NULL,
	[File_Date] [date] NULL
) ON [PRIMARY]

GO
