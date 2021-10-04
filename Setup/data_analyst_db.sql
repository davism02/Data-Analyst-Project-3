Create Table data_analyst_testing (
    "id" INT Primary Key,
    "Title" varchar (250) NOT NULL,
    "Salary" varchar (250) NOT NULL,
    "Rating" varchar NOT NULL,
    "Company" varchar (250) NOT NULL,
    "Location" varchar (250) NOT NULL,
    "Headquarters" varchar (250) NOT NULL,
    "Size" varchar (250) NOT NULL,
    "ownership" varchar (250) NOT NULL,
    "Industry" varchar (250) NOT NULL,
    "Sector" varchar (250) NOT NULL,
    "Revenue" varchar (250) NOT NULL,
    "min" float (1) NOT NULL,
    "max"  int NOT NULL
);
select * from data_analyst_testing