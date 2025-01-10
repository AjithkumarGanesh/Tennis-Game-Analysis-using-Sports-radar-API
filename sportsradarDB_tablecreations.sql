create database if not exists SportsRadarDB;
use SportsRadarDB;
create table if not exists Categories(
 category_id varchar(50) PRIMARY KEY,
 category_name VARCHAR(100) NOT NULL
 );
-- select * from Categories
create table if not exists Competitions(
 competition_id varchar(50) PRIMARY KEY,
 competition_name VARCHAR(10) NOT NULL,
 parent_id VARCHAR(50) NULL,
 type VARCHAR(20) NOT NULL,
 gender VARCHAR(10) NOT NULL,
 category_id varchar(50),
 FOREIGN KEY (category_id) REFERENCES Categories(category_id)
 ); 
-- select * from competitions;
create table if not exists Complexes(
 complex_id varchar(50) PRIMARY KEY,
 complex_name VARCHAR(100) NOT NULL
 ); 
-- select * from complexes;
create table if not exists Venues(
 venue_id varchar(50) PRIMARY KEY,
 venue_name VARCHAR(100) NOT NULL,
 city_name VARCHAR(100) NOT NULL,
 country_name VARCHAR(100) NOT NULL,
 country_code CHAR(3) NOT NULL,
 timezone VARCHAR(100) NOT NULL,
 complex_id varchar(50),
 FOREIGN KEY (complex_id) REFERENCES complexes(complex_id)
 ); 
-- select * from venues;
 create table if not exists Competitors(
 competitor_id VARCHAR(50) PRIMARY KEY,
 name VARCHAR(100) NOT NULL,
 country VARCHAR(100) NOT NULL,
 country_code char(3) NOT NULL,
 abbreviation VARCHAR(10) NOT NULL
  ); 
-- select * from competitors;
 create table if not exists Competitor_Rankings(
 rank_id int PRIMARY KEY,
 `rank` int NOT NULL,
 movement int NOT NULL,
 points int NOT NULL,
 competitons_played int NOT NULL,
 competitor_id VARCHAR(50),
 FOREIGN KEY (competitor_id) REFERENCES Competitors(competitor_id)
 ); 
-- select * from Competitor_Rankings;



 


