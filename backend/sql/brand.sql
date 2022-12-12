BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "brand" (
	"id"	INTEGER NOT NULL,
	"brand"	VARCHAR(100),
	"name"	VARCHAR(100),
	"price"	INTEGER,
	PRIMARY KEY("id")
);
INSERT INTO "brand" VALUES (1,'Abarth','Fiat 500',14699);
INSERT INTO "brand" VALUES (2,'Acura','ILX',16000);
INSERT INTO "brand" VALUES (3,'Acura','MDX',25075);
INSERT INTO "brand" VALUES (4,'Acura','RDX',23500);
INSERT INTO "brand" VALUES (5,'Acura','RL',7300);
INSERT INTO "brand" VALUES (6,'Acura','RLX',25250);
INSERT INTO "brand" VALUES (7,'Acura','RSX',5900);
INSERT INTO "brand" VALUES (8,'Acura','TL',14450);
INSERT INTO "brand" VALUES (9,'Acura','TLX',20900);
INSERT INTO "brand" VALUES (10,'Acura','TSX',11000);
INSERT INTO "brand" VALUES (11,'Acura','ZDX',17225);
INSERT INTO "brand" VALUES (12,'AION','V',39900);
INSERT INTO "brand" VALUES (13,'Alfa Romeo','159',8250);
INSERT INTO "brand" VALUES (14,'Alfa Romeo','164',2500);
INSERT INTO "brand" VALUES (15,'Alfa Romeo','166',3600);
INSERT INTO "brand" VALUES (16,'Alfa Romeo','Brera',17000);
INSERT INTO "brand" VALUES (17,'Alfa Romeo','Giulia',27500);
INSERT INTO "brand" VALUES (18,'Alfa Romeo','Giulietta',13325);
INSERT INTO "brand" VALUES (19,'Alfa Romeo','Stelvio',34500);
INSERT INTO "brand" VALUES (20,'Aston Martin','DB9',57000);
INSERT INTO "brand" VALUES (21,'Aston Martin','DBX',193000);
INSERT INTO "brand" VALUES (22,'Aston Martin','Rapide',123081);
INSERT INTO "brand" VALUES (23,'Aston Martin','Vantage',103800);
COMMIT;
