CREATE DATABASE IF NOT EXISTS `flask-db`;
USE `flask-db`;

SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS;
SET FOREIGN_KEY_CHECKS = 0;
SET NAMES utf8mb4;

CREATE TABLE IF NOT EXISTS `exercises` (
  `id` int NOT NULL AUTO_INCREMENT,
  `exercise` varchar(40) NOT NULL,
  `reps` varchar(20) NOT NULL,
  `completed` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `exercises` WRITE;

INSERT INTO `exercises` (`id`, `exercise`, `reps`, `completed`)
VALUES
	(1,'Legs','30',0),
	(2,'Arms','30',0),
	(3,'Abs','15',0),
	(4,'Upper','20',0),
	(5,'Lower','40',0),
	(6,'Neck','25',0);

UNLOCK TABLES;

CREATE TABLE IF NOT EXISTS `relationship` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fk_exercise` int DEFAULT NULL,
  `fk_workout` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_exercise` (`fk_exercise`),
  KEY `fk_workout` (`fk_workout`),
  CONSTRAINT `relationship_ibfk_1` FOREIGN KEY (`fk_exercise`) REFERENCES `exercises` (`id`),
  CONSTRAINT `relationship_ibfk_2` FOREIGN KEY (`fk_workout`) REFERENCES `workout_set` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


CREATE TABLE IF NOT EXISTS `workout_set` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `workout_set` WRITE;

INSERT INTO `workout_set` (`id`, `name`)
VALUES
	(1,'Short 10 min'),
	(2,'Medium 20 min'),
	(3,'Long 30 min'),
	(4,'Master Blaster 40 min');

UNLOCK TABLES;


SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;

