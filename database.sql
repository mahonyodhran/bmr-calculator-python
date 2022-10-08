CREATE DATABASE IF NOT EXISTS `bmr_calculator`;

USE `bmr_calculator`;

DROP TABLE IF EXISTS `calculated_bmr`;

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user`
  (
     `id`     INT(11) NOT NULL auto_increment,
     `age`    TINYINT NOT NULL,
     `weight` SMALLINT NOT NULL,
     `height` SMALLINT NOT NULL,
     `gender` CHAR(1) NOT NULL,
     `email`  VARCHAR(60) NOT NULL,
     PRIMARY KEY (`id`)
  )
engine=innodb
auto_increment=6
DEFAULT charset=latin1;

CREATE TABLE `calculated_bmr`
  (
     `id`      INT(11) NOT NULL auto_increment,
     `bmr`     SMALLINT NOT NULL,
     `user_id` INT(11) NOT NULL,
     PRIMARY KEY (`id`),
     CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES user(`id`)
  )
engine=innodb
auto_increment=6
DEFAULT charset=latin1; 