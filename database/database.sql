CREATE DATABASE IF NOT EXISTS `bmr_calculator`;

USE `bmr_calculator`;

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user`
  (
     `id`     INT(11) NOT NULL auto_increment,
     `age`    TINYINT NOT NULL,
     `weight` FLOAT NOT NULL,
     `height` SMALLINT NOT NULL,
     `gender` CHAR(1) NOT NULL,
     `bmr` SMALLINT NOT NULL,
     `email`  VARCHAR(60) DEFAULT NULL,
     PRIMARY KEY (`id`)
  )
engine=innodb
auto_increment=6
DEFAULT charset=latin1;

INSERT INTO `user`
VALUES (1,28, 100, 180,"m",1990, "test@mail.com");

INSERT INTO `user`
VALUES (2,25, 90, 150,"m",1718, "fake@mail.com");