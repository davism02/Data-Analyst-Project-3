CREATE TABLE "data_analyst" (
    "id" INT PRIMARY KEY,
	"Title" varchar(250)   NOT NULL,
    "Salary" varchar(250)   NOT NULL,
    "Rating" int   NOT NULL,
	"Company" varchar(50) NOT NULL,
	"Location" varchar(50) NOT NULL,
	"Headquarters" varchar(50) NOT NULL,
	"Size" varchar(50) NOT NULL,
	"Founded" varchar (50) NOT NULL,
	"ownership" varchar (250) NOT NULL,
	"Industry" varchar (250) NOT NULL,
	"Sector" varchar (50) NOT NULL,
	"Revenue" varchar (50) NOT NULL,
	"min" varchar (50) NOT NULL,
	"max" varchar (50) NOT NULL
     
) ;
select * From analyst