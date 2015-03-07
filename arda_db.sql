-- MySQL dump 10.13  Distrib 5.6.23, for osx10.8 (x86_64)
--
-- Host: localhost    Database: arda_db
-- ------------------------------------------------------
-- Server version	5.6.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ASSOCIATED_DISORDER`
--

DROP TABLE IF EXISTS `ASSOCIATED_DISORDER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ASSOCIATED_DISORDER` (
  `Name` varchar(100) NOT NULL,
  `Description` text,
  `RESOURCE_id` int(11) NOT NULL,
  PRIMARY KEY (`Name`,`RESOURCE_id`),
  KEY `fk_ASSOCIATED_DISORDER_RESOURCE1` (`RESOURCE_id`),
  CONSTRAINT `fk_ASSOCIATED_DISORDER_RESOURCE1` FOREIGN KEY (`RESOURCE_id`) REFERENCES `RESOURCE` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ASSOCIATED_DISORDER`
--

LOCK TABLES `ASSOCIATED_DISORDER` WRITE;
/*!40000 ALTER TABLE `ASSOCIATED_DISORDER` DISABLE KEYS */;
/*!40000 ALTER TABLE `ASSOCIATED_DISORDER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BEHAVIOR`
--

DROP TABLE IF EXISTS `BEHAVIOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BEHAVIOR` (
  `Name` varchar(100) NOT NULL,
  `Description` text,
  `RESOURCE_id` int(11) NOT NULL,
  PRIMARY KEY (`Name`,`RESOURCE_id`),
  KEY `fk_BEHAVIOR_RESOURCE1` (`RESOURCE_id`),
  CONSTRAINT `fk_BEHAVIOR_RESOURCE1` FOREIGN KEY (`RESOURCE_id`) REFERENCES `RESOURCE` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BEHAVIOR`
--

LOCK TABLES `BEHAVIOR` WRITE;
/*!40000 ALTER TABLE `BEHAVIOR` DISABLE KEYS */;
/*!40000 ALTER TABLE `BEHAVIOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `BORROWER`
--

DROP TABLE IF EXISTS `BORROWER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BORROWER` (
  `First_name` varchar(45) NOT NULL,
  `Last_name` varchar(45) DEFAULT NULL,
  `Email_address` varchar(45) DEFAULT NULL,
  `Reserved` tinyint(1) DEFAULT NULL,
  `Checkout_date` datetime DEFAULT NULL,
  `Return_date` datetime DEFAULT NULL,
  `LIBRARY_ITEM_RESOURCE_id` int(11) NOT NULL,
  PRIMARY KEY (`First_name`),
  KEY `fk_BORROWER_LIBRARY_ITEM1` (`LIBRARY_ITEM_RESOURCE_id`),
  CONSTRAINT `fk_BORROWER_LIBRARY_ITEM1` FOREIGN KEY (`LIBRARY_ITEM_RESOURCE_id`) REFERENCES `LIBRARY_ITEM` (`RESOURCE_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `BORROWER`
--

LOCK TABLES `BORROWER` WRITE;
/*!40000 ALTER TABLE `BORROWER` DISABLE KEYS */;
/*!40000 ALTER TABLE `BORROWER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EVENT`
--

DROP TABLE IF EXISTS `EVENT`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `EVENT` (
  `Location` varchar(100) NOT NULL,
  `RESOURCE_id` int(11) NOT NULL,
  PRIMARY KEY (`RESOURCE_id`),
  CONSTRAINT `fk_EVENT_RESOURCE1` FOREIGN KEY (`RESOURCE_id`) REFERENCES `RESOURCE` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EVENT`
--

LOCK TABLES `EVENT` WRITE;
/*!40000 ALTER TABLE `EVENT` DISABLE KEYS */;
/*!40000 ALTER TABLE `EVENT` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIBRARY_ITEM`
--

DROP TABLE IF EXISTS `LIBRARY_ITEM`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIBRARY_ITEM` (
  `Old_Item_id` int(11) NOT NULL,
  `Item_type` varchar(45) NOT NULL,
  `Author` varchar(45) DEFAULT NULL,
  `RESOURCE_id` int(11) NOT NULL,
  PRIMARY KEY (`RESOURCE_id`),
  CONSTRAINT `fk_LIBRARY_ITEM_RESOURCE1` FOREIGN KEY (`RESOURCE_id`) REFERENCES `RESOURCE` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIBRARY_ITEM`
--

LOCK TABLES `LIBRARY_ITEM` WRITE;
/*!40000 ALTER TABLE `LIBRARY_ITEM` DISABLE KEYS */;
/*!40000 ALTER TABLE `LIBRARY_ITEM` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ONLINE`
--

DROP TABLE IF EXISTS `ONLINE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ONLINE` (
  `Type` varchar(45) NOT NULL,
  `RESOURCE_id` int(11) NOT NULL,
  PRIMARY KEY (`RESOURCE_id`),
  CONSTRAINT `fk_ONLINE_RESOURCE1` FOREIGN KEY (`RESOURCE_id`) REFERENCES `RESOURCE` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ONLINE`
--

LOCK TABLES `ONLINE` WRITE;
/*!40000 ALTER TABLE `ONLINE` DISABLE KEYS */;
/*!40000 ALTER TABLE `ONLINE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `RESOURCE`
--

DROP TABLE IF EXISTS `RESOURCE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RESOURCE` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Phone_number` char(15) DEFAULT NULL,
  `Gender` char(1) NOT NULL,
  `Age_range` char(5) NOT NULL,
  `Description` text,
  `Category` varchar(100) NOT NULL,
  `Url` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `RESOURCE`
--

LOCK TABLES `RESOURCE` WRITE;
/*!40000 ALTER TABLE `RESOURCE` DISABLE KEYS */;
/*!40000 ALTER TABLE `RESOURCE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `THERAPY`
--

DROP TABLE IF EXISTS `THERAPY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `THERAPY` (
  `Location` varchar(100) DEFAULT NULL,
  `Insuarance_info` varchar(45) DEFAULT NULL,
  `RESOURCE_id` int(11) NOT NULL,
  `Expertise` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`RESOURCE_id`),
  CONSTRAINT `fk_THERAPY_RESOURCE1` FOREIGN KEY (`RESOURCE_id`) REFERENCES `RESOURCE` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `THERAPY`
--

LOCK TABLES `THERAPY` WRITE;
/*!40000 ALTER TABLE `THERAPY` DISABLE KEYS */;
/*!40000 ALTER TABLE `THERAPY` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-03-06 21:40:51
