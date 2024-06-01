CREATE DATABASE JJ;
USE [JJ]
GO

/****** Object:  Table [dbo].[Conferences]    Script Date: 5/27/2024 10:20:11 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Conferences](
	[Conference] [nvarchar](255) NULL,
	[CityCountry] [nvarchar](255) NULL,
	[Deadline] [nvarchar](1000) NULL,
	[Date] [nvarchar](255) NULL,
	[Website] [nvarchar](255) NULL,
	[Description] [nvarchar](255) NULL
) ON [PRIMARY]
GO


