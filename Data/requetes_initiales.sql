-- MySQL dump 10.13  Distrib 9.0.1, for macos14 (arm64)
--
-- Host: 127.0.0.1    Database: HockeyIQ
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `equipes`
--

DROP TABLE IF EXISTS `equipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipes` (
  `id_equipe` int NOT NULL AUTO_INCREMENT,
  `nom_equipe` varchar(100) DEFAULT NULL,
  `categorie` varchar(100) DEFAULT NULL,
  `saison` varchar(100) DEFAULT NULL,
  `position` int DEFAULT NULL,
  `matchs_joues` int DEFAULT NULL,
  `points` int DEFAULT NULL,
  `victoires_total` int DEFAULT NULL,
  `victoires_temps_regulier` int DEFAULT NULL,
  `victoires_fusillades` int DEFAULT NULL,
  `defaites` int DEFAULT NULL,
  `defaites_fusillades` int DEFAULT NULL,
  `nulles` int DEFAULT NULL,
  `buts_pour` int DEFAULT NULL,
  `buts_contre` int DEFAULT NULL,
  `differentiel` int DEFAULT NULL,
  `points_periode` int DEFAULT NULL,
  `points_partie` int DEFAULT NULL,
  `points_penalites` int DEFAULT NULL,
  `points_par_match` float DEFAULT NULL,
  PRIMARY KEY (`id_equipe`)
) ENGINE=InnoDB AUTO_INCREMENT=10207 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipes`
--

LOCK TABLES `equipes` WRITE;
/*!40000 ALTER TABLE `equipes` DISABLE KEYS */;
/*!40000 ALTER TABLE `equipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `joueurs`
--

DROP TABLE IF EXISTS `joueurs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `joueurs` (
  `id_joueur` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(100) DEFAULT NULL,
  `equipe` varchar(100) DEFAULT NULL,
  `matchs_joues` varchar(100) DEFAULT NULL,
  `buts` int DEFAULT NULL,
  `passes` int DEFAULT NULL,
  `points` int DEFAULT NULL,
  `minutes_penalite` varchar(100) DEFAULT NULL,
  `points_par_match` float DEFAULT NULL,
  `buts_avantage_numerique` int DEFAULT NULL,
  `points_avantage_numerique` int DEFAULT NULL,
  `buts_inferiorite_numerique` int DEFAULT NULL,
  `points_inferiorite_numerique` int DEFAULT NULL,
  `buts_gagnants` int DEFAULT NULL,
  `saison` varchar(100) DEFAULT NULL,
  `categorie` varchar(100) DEFAULT NULL,
  `position` int DEFAULT NULL,
  PRIMARY KEY (`id_joueur`)
) ENGINE=InnoDB AUTO_INCREMENT=58089 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `joueurs`
--

LOCK TABLES `joueurs` WRITE;
/*!40000 ALTER TABLE `joueurs` DISABLE KEYS */;
/*!40000 ALTER TABLE `joueurs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parties`
--

DROP TABLE IF EXISTS `parties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `parties` (
  `id_partie` int NOT NULL AUTO_INCREMENT,
  `categorie` varchar(100) DEFAULT NULL,
  `saison` varchar(100) DEFAULT NULL,
  `equipe_local` varchar(100) NOT NULL,
  `equipe_visiteur` varchar(100) NOT NULL,
  `score_local` int DEFAULT NULL,
  `score_visiteur` int DEFAULT NULL,
  `fusillades` tinyint(1) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `heure` time DEFAULT NULL,
  PRIMARY KEY (`id_partie`),
  UNIQUE KEY `unique_game` (`categorie`,`saison`,`equipe_local`,`equipe_visiteur`,`date`,`heure`),
  KEY `equipe_local_fk` (`equipe_local`),
  KEY `equipe_visiteur_fk` (`equipe_visiteur`)
) ENGINE=InnoDB AUTO_INCREMENT=26389 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parties`
--

LOCK TABLES `parties` WRITE;
/*!40000 ALTER TABLE `parties` DISABLE KEYS */;
INSERT INTO `parties` VALUES (18551,'B2','H2425','AS LMHO','brass bonanza',6,3,0,'2024-09-25','18:00:00'),(18552,'B2','H2425','Les Roses','Eagles',5,5,0,'2024-09-25','18:50:00'),(18553,'B2','H2425','Bulls','Les Miners',6,4,0,'2024-09-25','19:40:00'),(18554,'B2','H2425','SoluSimple Assurances HC','L’Antichambre (B2)',4,4,0,'2024-09-25','20:30:00'),(18555,'B2','H2425','Eagles','L’Antichambre (B2)',8,3,0,'2024-10-02','18:50:00'),(18556,'B2','H2425','brass bonanza','Bulls',0,10,0,'2024-10-02','19:40:00'),(18557,'B2','H2425','SoluSimple Assurances HC','AS LMHO',3,4,1,'2024-10-02','21:20:00'),(18558,'B2','H2425','Les Roses','Les Miners',7,6,1,'2024-10-02','22:10:00'),(18559,'B2','H2425','Bulls','SoluSimple Assurances HC',2,6,0,'2024-10-09','18:00:00'),(18560,'B2','H2425','Eagles','brass bonanza',8,3,0,'2024-10-09','18:50:00'),(18561,'B2','H2425','L’Antichambre (B2)','Les Miners',7,6,0,'2024-10-09','20:30:00'),(18562,'B2','H2425','AS LMHO','Les Roses',5,4,0,'2024-10-09','22:10:00'),(18563,'B2','H2425','Bulls','Eagles',8,2,0,'2024-10-16','18:00:00'),(18564,'B2','H2425','Les Miners','AS LMHO',4,8,0,'2024-10-16','18:50:00'),(18565,'B2','H2425','L’Antichambre (B2)','Les Roses',2,10,0,'2024-10-16','20:30:00'),(18566,'B2','H2425','brass bonanza','SoluSimple Assurances HC',0,7,0,'2024-10-16','21:20:00'),(18567,'B2','H2425','Les Roses','Bulls',4,7,0,'2024-10-23','19:40:00'),(18568,'B2','H2425','Eagles','AS LMHO',6,4,0,'2024-10-23','20:30:00'),(18569,'B2','H2425','Les Miners','SoluSimple Assurances HC',4,12,0,'2024-10-23','21:20:00'),(18570,'B2','H2425','brass bonanza','L’Antichambre (B2)',5,3,0,'2024-10-23','22:10:00'),(18571,'B2','H2425','Eagles','Les Roses',6,4,0,'2024-10-30','18:00:00'),(18572,'B2','H2425','brass bonanza','Bulls',7,3,0,'2024-10-30','18:50:00'),(18573,'B2','H2425','L’Antichambre (B2)','SoluSimple Assurances HC',1,11,0,'2024-10-30','20:30:00'),(18574,'B2','H2425','AS LMHO','Les Miners',5,2,0,'2024-10-30','22:10:00'),(18575,'B2','H2425','SoluSimple Assurances HC','Bulls',6,5,0,'2024-11-06','18:00:00'),(18576,'B2','H2425','L’Antichambre (B2)','Les Roses',4,2,0,'2024-11-06','19:40:00'),(18577,'B2','H2425','AS LMHO','brass bonanza',7,1,0,'2024-11-06','20:30:00'),(18578,'B2','H2425','Les Miners','Eagles',6,10,0,'2024-11-06','22:10:00'),(18579,'B2','H2425','Les Miners','L’Antichambre (B2)',2,11,0,'2024-11-13','18:00:00'),(18580,'B2','H2425','SoluSimple Assurances HC','Les Roses',9,5,0,'2024-11-13','18:50:00'),(18581,'B2','H2425','Eagles','brass bonanza',9,6,0,'2024-11-13','20:30:00'),(18582,'B2','H2425','Bulls','AS LMHO',5,1,0,'2024-11-13','22:10:00'),(18583,'B2','H2425','SoluSimple Assurances HC','AS LMHO',2,7,0,'2024-11-20','18:50:00'),(18584,'B2','H2425','Eagles','Les Miners',7,7,0,'2024-11-20','19:40:00'),(18585,'B2','H2425','Bulls','Les Roses',3,5,0,'2024-11-20','20:30:00'),(18586,'B2','H2425','L’Antichambre (B2)','brass bonanza',8,4,0,'2024-11-20','22:10:00'),(18587,'B2','H2425','Bulls','AS LMHO',2,3,1,'2024-11-27','18:50:00'),(18588,'B2','H2425','SoluSimple Assurances HC','Les Roses',4,5,1,'2024-11-27','19:40:00'),(18589,'B2','H2425','brass bonanza','Les Miners',10,5,0,'2024-11-27','20:30:00'),(18590,'B2','H2425','L’Antichambre (B2)','Eagles',6,3,0,'2024-11-27','21:20:00'),(18591,'B2','H2425','brass bonanza','L’Antichambre (B2)',5,8,0,'2024-12-04','18:00:00'),(18592,'B2','H2425','AS LMHO','Les Roses',10,1,0,'2024-12-04','18:50:00'),(18593,'B2','H2425','Les Miners','Eagles',5,8,0,'2024-12-04','20:30:00'),(18594,'B2','H2425','SoluSimple Assurances HC','Bulls',6,2,0,'2024-12-04','22:10:00'),(18595,'B2','H2425','Les Roses','brass bonanza',2,5,0,'2024-12-11','19:40:00'),(18596,'B2','H2425','AS LMHO','Eagles',4,7,0,'2024-12-11','19:40:00'),(18597,'B2','H2425','Bulls','L’Antichambre (B2)',7,4,0,'2024-12-11','21:20:00'),(18598,'B2','H2425','Les Miners','SoluSimple Assurances HC',3,7,0,'2024-12-11','22:10:00'),(18599,'B2','H2425','brass bonanza','SoluSimple Assurances HC',2,10,0,'2024-12-18','19:40:00'),(18600,'B2','H2425','Bulls','Eagles',5,5,0,'2024-12-18','20:30:00'),(18601,'B2','H2425','Les Roses','Les Miners',3,4,0,'2024-12-18','21:20:00'),(18602,'B2','H2425','AS LMHO','L’Antichambre (B2)',2,6,0,'2024-12-18','22:10:00'),(18603,'B2','H2425','Les Roses','Les Miners',6,3,0,'2025-01-08','18:00:00'),(18604,'B2','H2425','SoluSimple Assurances HC','Eagles',9,8,0,'2025-01-08','18:50:00'),(18605,'B2','H2425','Bulls','brass bonanza',4,7,0,'2025-01-08','20:30:00'),(18606,'B2','H2425','AS LMHO','L’Antichambre (B2)',6,3,0,'2025-01-08','21:20:00'),(18607,'B2','H2425','AS LMHO','Les Miners',7,1,0,'2025-01-15','18:50:00'),(18608,'B2','H2425','Bulls','Eagles',5,12,0,'2025-01-15','19:40:00'),(18609,'B2','H2425','L’Antichambre (B2)','Les Roses',2,7,0,'2025-01-15','21:20:00'),(18610,'B2','H2425','brass bonanza','SoluSimple Assurances HC',2,4,0,'2025-01-15','22:10:00'),(18611,'B2','H2425','brass bonanza','Les Roses',4,6,0,'2025-01-22','18:00:00'),(18612,'B2','H2425','L’Antichambre (B2)','Eagles',8,6,0,'2025-01-22','18:00:00'),(18613,'B2','H2425','SoluSimple Assurances HC','Les Miners',13,5,0,'2025-01-22','19:40:00'),(18614,'B2','H2425','Bulls','AS LMHO',3,8,0,'2025-01-22','20:30:00'),(18615,'B2','H2425','AS LMHO','SoluSimple Assurances HC',4,5,1,'2025-01-29','18:00:00'),(18616,'B2','H2425','L’Antichambre (B2)','Bulls',5,6,1,'2025-01-29','18:50:00'),(18617,'B2','H2425','brass bonanza','Les Miners',3,12,0,'2025-01-29','20:30:00'),(18618,'B2','H2425','Les Roses','Eagles',4,7,0,'2025-01-29','22:10:00'),(18619,'B2','H2425','AS LMHO','brass bonanza',3,2,0,'2025-02-05','18:00:00'),(18620,'B2','H2425','Les Miners','L’Antichambre (B2)',11,8,0,'2025-02-05','20:30:00'),(18621,'B2','H2425','Bulls','Eagles',8,0,0,'2025-02-05','21:20:00'),(18622,'B2','H2425','Les Roses','SoluSimple Assurances HC',5,4,1,'2025-02-05','22:10:00'),(18623,'B2','H2425','Les Roses','AS LMHO',5,4,0,'2025-02-12','18:00:00'),(18624,'B2','H2425','brass bonanza','Eagles',3,8,0,'2025-02-12','19:40:00'),(18625,'B2','H2425','SoluSimple Assurances HC','Les Miners',10,4,0,'2025-02-12','21:20:00'),(18626,'B2','H2425','Bulls','L’Antichambre (B2)',4,1,0,'2025-02-12','22:10:00'),(18627,'B2','H2425','L’Antichambre (B2)','AS LMHO',5,4,1,'2025-02-19','18:50:00'),(18628,'B2','H2425','Eagles','SoluSimple Assurances HC',3,6,0,'2025-02-19','19:40:00'),(18629,'B2','H2425','Les Roses','Bulls',4,6,0,'2025-02-19','20:30:00'),(18630,'B2','H2425','Les Miners','brass bonanza',5,6,1,'2025-02-19','21:20:00'),(18631,'B2','H2425','Les Miners','Eagles',7,11,0,'2025-02-26','18:00:00'),(18632,'B2','H2425','SoluSimple Assurances HC','Les Roses',5,4,0,'2025-02-26','18:50:00'),(18633,'B2','H2425','L’Antichambre (B2)','Bulls',1,5,0,'2025-02-26','19:40:00'),(18634,'B2','H2425','AS LMHO','brass bonanza',4,2,0,'2025-02-26','20:30:00'),(18635,'B2','H2425','Bulls','Les Miners',10,8,0,'2025-03-05','18:00:00'),(18636,'B2','H2425','Eagles','AS LMHO',2,3,1,'2025-03-05','18:50:00'),(18637,'B2','H2425','SoluSimple Assurances HC','L’Antichambre (B2)',7,3,0,'2025-03-05','19:40:00'),(18638,'B2','H2425','brass bonanza','Les Roses',3,4,0,'2025-03-05','21:20:00'),(18639,'B2','H2425','SoluSimple Assurances HC','L’Antichambre (B2)',6,4,0,'2025-03-12','18:00:00'),(18640,'B2','H2425','Bulls','Les Miners',5,8,0,'2025-03-12','20:30:00'),(18641,'B2','H2425','Les Roses','AS LMHO',0,4,0,'2025-03-12','21:20:00'),(18642,'B2','H2425','Eagles','brass bonanza',7,2,0,'2025-03-12','22:10:00'),(18643,'B2','H2425','SoluSimple Assurances HC','Eagles',9,3,0,'2025-03-19','18:50:00'),(18644,'B2','H2425','AS LMHO','L’Antichambre (B2)',4,7,0,'2025-03-19','19:40:00'),(18645,'B2','H2425','Les Miners','Les Roses',3,5,0,'2025-03-19','20:30:00'),(18646,'B2','H2425','Bulls','brass bonanza',7,3,0,'2025-03-19','21:20:00'),(18647,'B3','H2425','Les Tchums','Caps',5,3,0,'2024-09-24','19:40:00'),(18648,'B3','H2425','Létourno Pneus et Mécanique','L’Antichambre (B3)',5,2,0,'2024-09-24','22:10:00'),(18649,'B3','H2425','Phoenix (B3)','Benchwarmers (B3)',4,9,0,'2024-09-25','21:20:00'),(18650,'B3','H2425','High School','Brown and Gold',2,7,0,'2024-09-27','21:20:00'),(18651,'B3','H2425','High School','Aliments LAD (B3)',4,7,0,'2024-09-29','09:10:00'),(18652,'B3','H2425','Benchwarmers (B3)','K2D Assurances (B3)',3,2,0,'2024-09-29','14:10:00'),(18653,'B3','H2425','Létourno Pneus et Mécanique','Les Tchums',3,2,0,'2024-09-29','17:40:00'),(18654,'B3','H2425','Brown and Gold','Caps',7,0,0,'2024-09-29','21:50:00'),(18655,'B3','H2425','Phoenix (B3)','Aliments LAD (B3)',6,9,0,'2024-09-30','20:30:00'),(18656,'B3','H2425','Benchwarmers (B3)','Aliments LAD (B3)',5,13,0,'2024-10-06','14:50:00'),(18657,'B3','H2425','Caps','L’Antichambre (B3)',9,5,0,'2024-10-06','17:20:00'),(18658,'B3','H2425','Les Tchums','High School',6,3,0,'2024-10-06','18:10:00'),(18659,'B3','H2425','Brown and Gold','Létourno Pneus et Mécanique',5,6,0,'2024-10-06','19:50:00'),(18660,'B3','H2425','K2D Assurances (B3)','Phoenix (B3)',2,2,0,'2024-10-09','21:20:00'),(18661,'B3','H2425','Benchwarmers (B3)','Létourno Pneus et Mécanique',0,2,0,'2024-10-13','15:40:00'),(18662,'B3','H2425','Caps','High School',3,5,0,'2024-10-13','16:30:00'),(18663,'B3','H2425','K2D Assurances (B3)','L’Antichambre (B3)',2,2,0,'2024-10-13','17:20:00'),(18664,'B3','H2425','Aliments LAD (B3)','Brown and Gold',4,6,0,'2024-10-13','19:50:00'),(18665,'B3','H2425','L’Antichambre (B3)','High School',2,6,0,'2024-10-14','18:50:00'),(18666,'B3','H2425','Phoenix (B3)','Les Tchums',9,4,0,'2024-10-14','22:10:00'),(18667,'B3','H2425','K2D Assurances (B3)','Benchwarmers (B3)',2,3,0,'2024-10-17','18:00:00'),(18668,'B3','H2425','Aliments LAD (B3)','Caps',9,4,0,'2024-10-17','19:40:00'),(18669,'B3','H2425','Létourno Pneus et Mécanique','Brown and Gold',1,5,0,'2024-10-17','20:30:00'),(18670,'B3','H2425','High School','Benchwarmers (B3)',12,3,0,'2024-10-21','18:00:00'),(18671,'B3','H2425','L’Antichambre (B3)','Les Tchums',5,3,0,'2024-10-21','19:40:00'),(18672,'B3','H2425','Caps','Brown and Gold',5,4,1,'2024-10-21','22:10:00'),(18673,'B3','H2425','K2D Assurances (B3)','Létourno Pneus et Mécanique',2,3,0,'2024-10-22','19:40:00'),(18674,'B3','H2425','Aliments LAD (B3)','Phoenix (B3)',11,4,0,'2024-10-22','20:30:00'),(18675,'B3','H2425','L’Antichambre (B3)','Brown and Gold',6,6,0,'2024-10-28','18:00:00'),(18676,'B3','H2425','K2D Assurances (B3)','Caps',2,6,1,'2024-10-28','20:30:00'),(18677,'B3','H2425','Phoenix (B3)','High School',6,3,0,'2024-10-28','21:20:00'),(18678,'B3','H2425','Aliments LAD (B3)','Létourno Pneus et Mécanique',2,9,0,'2024-10-29','21:20:00'),(18679,'B3','H2425','Brown and Gold','Phoenix (B3)',12,4,0,'2024-11-01','18:00:00'),(18680,'B3','H2425','L’Antichambre (B3)','K2D Assurances (B3)',5,2,1,'2024-11-01','18:50:00'),(18681,'B3','H2425','Les Tchums','Caps',4,5,0,'2024-11-01','20:30:00'),(18682,'B3','H2425','Les Tchums','K2D Assurances (B3)',2,2,0,'2024-11-04','22:10:00'),(18683,'B3','H2425','Létourno Pneus et Mécanique','Caps',12,6,0,'2024-11-05','18:50:00'),(18684,'B3','H2425','L’Antichambre (B3)','Aliments LAD (B3)',4,5,1,'2024-11-05','22:10:00'),(18685,'B3','H2425','High School','Aliments LAD (B3)',3,2,1,'2024-11-07','21:20:00'),(18686,'B3','H2425','K2D Assurances (B3)','Les Tchums',2,4,1,'2024-11-08','18:00:00'),(18687,'B3','H2425','L’Antichambre (B3)','Phoenix (B3)',4,4,0,'2024-11-08','21:20:00'),(18688,'B3','H2425','High School','Létourno Pneus et Mécanique',2,6,0,'2024-11-10','19:00:00'),(18689,'B3','H2425','Caps','K2D Assurances (B3)',5,2,0,'2024-11-12','19:40:00'),(18690,'B3','H2425','Phoenix (B3)','Brown and Gold',1,8,0,'2024-11-12','20:30:00'),(18691,'B3','H2425','Les Tchums','L’Antichambre (B3)',5,2,0,'2024-11-13','19:40:00'),(18692,'B3','H2425','Caps','High School',3,10,0,'2024-11-15','18:00:00'),(18693,'B3','H2425','Létourno Pneus et Mécanique','Aliments LAD (B3)',6,5,0,'2024-11-15','19:40:00'),(18694,'B3','H2425','Phoenix (B3)','K2D Assurances (B3)',1,2,0,'2024-11-17','11:40:00'),(18695,'B3','H2425','Brown and Gold','Les Tchums',7,3,0,'2024-11-17','19:20:00'),(18696,'B3','H2425','Létourno Pneus et Mécanique','Caps',5,3,0,'2024-11-19','18:50:00'),(18697,'B3','H2425','High School','Les Tchums',2,1,0,'2024-11-20','18:50:00'),(18698,'B3','H2425','L’Antichambre (B3)','Aliments LAD (B3)',3,9,0,'2024-11-24','19:20:00'),(18699,'B3','H2425','Les Tchums','Aliments LAD (B3)',3,2,0,'2024-11-26','19:40:00'),(18700,'B3','H2425','Brown and Gold','Caps',7,6,1,'2024-11-26','20:30:00'),(18701,'B3','H2425','K2D Assurances (B3)','Létourno Pneus et Mécanique',2,5,0,'2024-11-26','21:20:00'),(18702,'B3','H2425','Phoenix (B3)','L’Antichambre (B3)',5,8,0,'2024-11-27','18:00:00'),(18703,'B3','H2425','Brown and Gold','High School',8,1,0,'2024-11-28','19:40:00'),(18704,'B3','H2425','Phoenix (B3)','Caps',4,4,0,'2024-12-01','12:30:00'),(18705,'B3','H2425','Les Tchums','Brown and Gold',2,5,0,'2024-12-03','18:00:00'),(18706,'B3','H2425','K2D Assurances (B3)','Aliments LAD (B3)',2,7,0,'2024-12-06','18:50:00'),(18707,'B3','H2425','Létourno Pneus et Mécanique','High School',3,2,1,'2024-12-08','21:00:00'),(18708,'B3','H2425','Caps','L’Antichambre (B3)',3,6,0,'2024-12-10','18:00:00'),(18709,'B3','H2425','Létourno Pneus et Mécanique','Phoenix (B3)',10,1,0,'2024-12-10','19:40:00'),(18710,'B3','H2425','K2D Assurances (B3)','Brown and Gold',2,8,0,'2024-12-12','20:30:00'),(18711,'B3','H2425','Aliments LAD (B3)','Caps',6,5,0,'2024-12-12','21:20:00'),(18712,'B3','H2425','L’Antichambre (B3)','High School',2,3,0,'2024-12-12','22:10:00'),(18713,'B3','H2425','Les Tchums','Aliments LAD (B3)',3,5,0,'2024-12-15','12:30:00'),(18714,'B3','H2425','Les Tchums','Létourno Pneus et Mécanique',3,5,0,'2024-12-18','18:00:00'),(18715,'B3','H2425','Caps','Phoenix (B3)',3,0,0,'2024-12-18','22:10:00'),(18716,'B3','H2425','Phoenix (B3)','Létourno Pneus et Mécanique',3,9,0,'2024-12-22','09:10:00'),(18717,'B3','H2425','High School','Brown and Gold',2,4,0,'2024-12-22','19:20:00'),(18718,'B3','H2425','Aliments LAD (B3)','K2D Assurances (B3)',5,2,0,'2024-12-29','21:50:00'),(18719,'B3','H2425','Phoenix (B3)','Brown and Gold',3,8,0,'2024-12-30','21:20:00'),(18720,'B3','H2425','Aliments LAD (B3)','L’Antichambre (B3)',5,3,0,'2025-01-07','22:10:00'),(18721,'B3','H2425','High School','Caps',7,6,0,'2025-01-08','18:00:00'),(18722,'B3','H2425','Brown and Gold','L’Antichambre (B3)',6,4,0,'2025-01-09','21:20:00'),(18723,'B3','H2425','Les Tchums','Phoenix (B3)',10,6,0,'2025-01-10','20:30:00'),(18724,'B3','H2425','Aliments LAD (B3)','Phoenix (B3)',8,5,0,'2025-01-12','11:40:00'),(18725,'B3','H2425','Létourno Pneus et Mécanique','K2D Assurances (B3)',7,2,0,'2025-01-12','20:10:00'),(18726,'B3','H2425','K2D Assurances (B3)','L’Antichambre (B3)',2,4,0,'2025-01-13','21:20:00'),(18727,'B3','H2425','Brown and Gold','High School',6,7,1,'2025-01-13','22:10:00'),(18728,'B3','H2425','Les Tchums','Caps',4,8,0,'2025-01-19','16:50:00'),(18729,'B3','H2425','Aliments LAD (B3)','Brown and Gold',7,9,0,'2025-01-20','19:40:00'),(18730,'B3','H2425','Caps','K2D Assurances (B3)',7,2,0,'2025-01-21','18:00:00'),(18731,'B3','H2425','Létourno Pneus et Mécanique','Phoenix (B3)',8,2,0,'2025-01-21','20:30:00'),(18732,'B3','H2425','Brown and Gold','Létourno Pneus et Mécanique',10,6,0,'2025-01-24','18:50:00'),(18733,'B3','H2425','Phoenix (B3)','Les Tchums',4,6,0,'2025-01-26','11:40:00'),(18734,'B3','H2425','Caps','L’Antichambre (B3)',5,4,1,'2025-01-26','16:50:00'),(18735,'B3','H2425','K2D Assurances (B3)','High School',2,1,0,'2025-01-26','21:00:00'),(18736,'B3','H2425','Les Tchums','Brown and Gold',8,6,0,'2025-01-27','18:50:00'),(18737,'B3','H2425','Caps','Phoenix (B3)',1,5,0,'2025-01-29','19:40:00'),(18738,'B3','H2425','High School','Aliments LAD (B3)',2,7,0,'2025-01-31','19:40:00'),(18739,'B3','H2425','Létourno Pneus et Mécanique','L’Antichambre (B3)',7,1,0,'2025-01-31','20:30:00'),(18740,'B3','H2425','Brown and Gold','K2D Assurances (B3)',5,2,0,'2025-02-02','21:50:00'),(18741,'B3','H2425','Caps','Létourno Pneus et Mécanique',3,12,0,'2025-02-05','18:00:00'),(18742,'B3','H2425','Les Tchums','Aliments LAD (B3)',3,4,0,'2025-02-05','19:40:00'),(18743,'B3','H2425','High School','K2D Assurances (B3)',7,2,1,'2025-02-09','10:50:00'),(18744,'B3','H2425','Létourno Pneus et Mécanique','Phoenix (B3)',6,7,0,'2025-02-12','18:00:00'),(18745,'B3','H2425','K2D Assurances (B3)','Les Tchums',2,6,0,'2025-02-12','20:30:00'),(18746,'B3','H2425','Aliments LAD (B3)','K2D Assurances (B3)',8,2,0,'2025-02-17','18:00:00'),(18747,'B3','H2425','Les Tchums','Caps',2,7,0,'2025-02-17','22:10:00'),(18748,'B3','H2425','Brown and Gold','Aliments LAD (B3)',5,4,1,'2025-02-24','18:50:00'),(18749,'B3','H2425','L’Antichambre (B3)','Phoenix (B3)',4,3,1,'2025-02-24','19:40:00'),(18750,'B3','H2425','Les Tchums','Létourno Pneus et Mécanique',4,3,0,'2025-02-26','21:20:00'),(18751,'B3','H2425','K2D Assurances (B3)','Aliments LAD (B3)',2,8,0,'2025-02-28','18:50:00'),(18752,'B3','H2425','High School','L’Antichambre (B3)',6,4,0,'2025-02-28','21:20:00'),(18753,'B3','H2425','Caps','Brown and Gold',7,6,0,'2025-03-02','19:20:00'),(18754,'B3','H2425','Phoenix (B3)','High School',0,3,0,'2025-03-05','22:10:00'),(18755,'B3','H2425','L’Antichambre (B3)','Les Tchums',7,3,0,'2025-03-09','15:00:00'),(18756,'B3','H2425','Aliments LAD (B3)','Létourno Pneus et Mécanique',7,8,1,'2025-03-09','17:40:00'),(18757,'B3','H2425','Phoenix (B3)','High School',6,7,1,'2025-03-10','18:50:00'),(18758,'B3','H2425','Les Tchums','Létourno Pneus et Mécanique',0,3,0,'2025-03-11','22:10:00'),(18759,'B3','H2425','Aliments LAD (B3)','Caps',11,1,0,'2025-03-12','20:30:00'),(18760,'B3','H2425','Brown and Gold','K2D Assurances (B3)',7,2,0,'2025-03-13','21:20:00'),(18761,'B3','H2425','High School','Létourno Pneus et Mécanique',6,9,0,'2025-03-14','19:40:00'),(18762,'B3','H2425','L’Antichambre (B3)','Caps',2,2,0,'2025-03-16','10:50:00'),(18763,'B3','H2425','Brown and Gold','Les Tchums',9,1,0,'2025-03-16','19:20:00'),(18764,'B3','H2425','Phoenix (B3)','Aliments LAD (B3)',4,6,0,'2025-03-17','22:10:00'),(18765,'B3','H2425','L’Antichambre (B3)','Létourno Pneus et Mécanique',5,7,0,'2025-03-18','18:00:00'),(18766,'B3','H2425','K2D Assurances (B3)','High School',2,6,0,'2025-03-24','20:30:00'),(18767,'B3','H2425','Phoenix (B3)','Caps',6,7,1,'2025-03-26','19:40:00'),(18768,'B3','H2425','Les Tchums','Aliments LAD (B3)',5,4,1,'2025-03-28','18:00:00'),(18769,'B3','H2425','L’Antichambre (B3)','Phoenix (B3)',5,4,1,'2025-03-30','09:10:00'),(18770,'B3','H2425','High School','Létourno Pneus et Mécanique',3,5,0,'2025-03-30','15:00:00'),(18771,'B3','H2425','K2D Assurances (B3)','Brown and Gold',2,5,0,'2025-03-30','21:50:00'),(18772,'B3','H2425','High School','Aliments LAD (B3)',2,4,0,'2025-04-02','19:40:00'),(18773,'B3','H2425','Les Tchums','L’Antichambre (B3)',3,1,0,'2025-04-02','21:20:00'),(18774,'B3','H2425','Létourno Pneus et Mécanique','L’Antichambre (B3)',11,2,0,'2025-04-03','19:40:00'),(18775,'B3','H2425','Létourno Pneus et Mécanique','Caps',4,5,0,'2025-04-04','21:20:00'),(18776,'B3','H2425','Caps','High School',3,8,0,'2025-04-06','09:10:00'),(18777,'B3','H2425','Phoenix (B3)','Les Tchums',1,7,0,'2025-04-06','10:50:00'),(18778,'B3','H2425','K2D Assurances (B3)','L’Antichambre (B3)',2,2,0,'2025-04-06','18:30:00'),(18779,'B3','H2425','High School','Les Tchums',6,4,0,'2025-04-07','18:50:00'),(18780,'B3','H2425','Aliments LAD (B3)','Brown and Gold',7,8,1,'2025-04-08','18:00:00'),(18781,'B3','H2425','K2D Assurances (B3)','Phoenix (B3)',2,3,0,'2025-04-08','19:40:00'),(18782,'B3','H2425','L’Antichambre (B3)','Brown and Gold',5,9,0,'2025-04-10','18:00:00'),(18783,'B3','H2425','K2D Assurances (B3)','High School',2,4,0,'2025-04-10','18:00:00'),(23573,'B3','H2425','Brown and Gold','L’Antichambre (B3)',9,6,0,'2025-04-14','20:30:00');
/*!40000 ALTER TABLE `parties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `predictions`
--

DROP TABLE IF EXISTS `predictions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `predictions` (
  `prediction_id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `game_id` int NOT NULL,
  `user_correct` tinyint(1) DEFAULT NULL,
  `computer_correct` varchar(100) DEFAULT NULL,
  `user_prediction` varchar(100) DEFAULT NULL,
  `computer_prediction` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`prediction_id`),
  UNIQUE KEY `prediction_id` (`prediction_id`),
  KEY `user_id` (`user_id`),
  KEY `game_id` (`game_id`),
  CONSTRAINT `predictions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `utilisateurs` (`id_utilisateur`),
  CONSTRAINT `predictions_ibfk_2` FOREIGN KEY (`game_id`) REFERENCES `parties` (`id_partie`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `predictions`
--

LOCK TABLES `predictions` WRITE;
/*!40000 ALTER TABLE `predictions` DISABLE KEYS */;
/*!40000 ALTER TABLE `predictions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `utilisateurs`
--

DROP TABLE IF EXISTS `utilisateurs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `utilisateurs` (
  `prenom` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mot_de_passe` varchar(100) DEFAULT NULL,
  `id_utilisateur` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_utilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `utilisateurs`
--

LOCK TABLES `utilisateurs` WRITE;
/*!40000 ALTER TABLE `utilisateurs` DISABLE KEYS */;
INSERT INTO `utilisateurs` VALUES ('Gabrielle','gabriellebeaupre2004@hotmail.com','9062ae750220c4740a8ab9df21c119f0c61e62bbcdd8819ead1f5cd6bf8a1cad',18),('lu','luciechagnon14@gmail.com','ae29fe576d3073321d4f4710cca4f481a16d3e732dbc1ef2141b5ce2df4c0ff8',22),('Felix','felixquirion72@gmail.com','02d834937940afd612fe9ad368b78ec3b4fb56fdefc0998c5f9b0c3b2a94a703',24),('Loïc ','ltherrien4@icloud.com','d11ae7cc9c7e391eb6a625abecca08247b76f8bb2390bf9a77023282be37d480',25),('Alex','alexdion2007@hotmail.com','290d4791df9c727b465fd1ba9d0d429b28460083ec18ee3e45e30a8226ab4dd7',28),('Alexandre','alexandre15roy@gmail.com','d6fd8c626f7cc90d27c68721b4cb4abd63f9cabb55dc24b6dddaed7b22153858',39);
/*!40000 ALTER TABLE `utilisateurs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-07 15:47:02
