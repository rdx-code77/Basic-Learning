-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 02, 2019 at 07:48 AM
-- Server version: 5.7.23
-- PHP Version: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `registration`
--

DELIMITER $$
--
-- Procedures
--
DROP PROCEDURE IF EXISTS `delete_data`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `delete_data` (IN `sid` INT(20))  BEGIN
DELETE FROM owners WHERE owners.sid=sid ;
END$$

DROP PROCEDURE IF EXISTS `update_data`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `update_data` (IN `sid` INT(20), IN `nemail` VARCHAR(50))  BEGIN
UPDATE owners SET owners.email=nemail WHERE owners.sid=sid;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
CREATE TABLE IF NOT EXISTS `admin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('admin', '123');

-- --------------------------------------------------------

--
-- Table structure for table `bidders`
--

DROP TABLE IF EXISTS `bidders`;
CREATE TABLE IF NOT EXISTS `bidders` (
  `name` varchar(50) NOT NULL,
  `shopid` int(20) NOT NULL,
  `bcost` int(20) NOT NULL,
  `datee` date NOT NULL,
  `cid` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `phno` int(20) NOT NULL,
  PRIMARY KEY (`phno`),
  KEY `shopid` (`shopid`),
  KEY `cid` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bidders`
--

INSERT INTO `bidders` (`name`, `shopid`, `bcost`, `datee`, `cid`, `qty`, `phno`) VALUES
('ameshmb', 10, 3750, '2019-12-01', 4, 15, 121212),
('ameshmb', 1, 500, '2019-11-29', 1, 5, 12451245),
('manojj', 1, 12500, '2019-12-02', 1, 50, 147852369),
('amesh', 10, 2000, '2019-12-01', 4, 10, 911357298),
('mnk', 1, 18000, '2019-12-04', 1, 60, 1236951478);

-- --------------------------------------------------------

--
-- Table structure for table `crops`
--

DROP TABLE IF EXISTS `crops`;
CREATE TABLE IF NOT EXISTS `crops` (
  `cid` int(20) NOT NULL,
  `toc` varchar(50) NOT NULL,
  `price` int(20) NOT NULL,
  PRIMARY KEY (`cid`,`toc`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `crops`
--

INSERT INTO `crops` (`cid`, `toc`, `price`) VALUES
(1, 'rice', 100),
(2, 'chicken', 0),
(3, 'wheet', 50),
(4, 'apricot', 143),
(5, 'ragi', 0);

-- --------------------------------------------------------

--
-- Table structure for table `fd`
--

DROP TABLE IF EXISTS `fd`;
CREATE TABLE IF NOT EXISTS `fd` (
  `name` varchar(50) NOT NULL,
  `qty` int(20) NOT NULL,
  `sold` int(20) NOT NULL,
  `phno` int(11) NOT NULL,
  `sid` int(20) NOT NULL,
  `date` date NOT NULL,
  `cid` int(20) NOT NULL,
  PRIMARY KEY (`phno`),
  KEY `sid` (`sid`),
  KEY `cid` (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `fd`
--

INSERT INTO `fd` (`name`, `qty`, `sold`, `phno`, `sid`, `date`, `cid`) VALUES
('a', 12, 1080, 122222, 1, '2019-11-29', 1),
('ganesh', 20, 2860, 1233331, 10, '2019-12-01', 4),
('abc', 5, 1000, 1233337, 1, '2019-11-28', 2),
('abc', 10, 1430, 12333371, 10, '2019-12-01', 4),
('abcd', 55, 5500, 12542514, 1, '2019-12-02', 1),
('b', 60, 6000, 126987543, 1, '2019-12-03', 1);

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

DROP TABLE IF EXISTS `logs`;
CREATE TABLE IF NOT EXISTS `logs` (
  `SNo` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) NOT NULL,
  `action` varchar(50) NOT NULL,
  `date_time` datetime NOT NULL,
  PRIMARY KEY (`SNo`)
) ENGINE=MyISAM AUTO_INCREMENT=122 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`SNo`, `email`, `action`, `date_time`) VALUES
(121, 'mmm@gmail.com', 'UPDATED AT', '2019-12-02 13:04:44'),
(120, 'haaa@gmail.com', 'UPDATED AT', '2019-12-02 13:00:02'),
(119, 'hiii@gmail.com', 'REGISTERED AT', '2019-12-02 12:59:02'),
(118, 's10@gmail.com', 'UPDATED AT', '2019-12-01 14:19:24'),
(117, 'shop10@gmail.com', 'REGISTERED AT', '2019-12-01 14:18:52'),
(116, 'shopd@gmail.com', 'REGISTERED AT', '2019-12-01 11:20:54'),
(115, 'shpc@gmail.com', 'REGISTERED AT', '2019-11-30 12:05:46'),
(114, 'shopb@gmail.com', 'REGISTERED AT', '2019-11-30 12:03:41'),
(113, 'd@gmail.com', 'DELETED AT', '2019-11-30 12:02:09'),
(112, 'd@gmail.com', 'REGISTERED AT', '2019-11-30 12:00:18'),
(111, 'a@gmail.com', 'DELETED AT', '2019-11-25 00:35:36'),
(110, 'sb@gmail.com', 'DELETED AT', '2019-11-25 00:23:22'),
(109, 'shopa@gmail.com', 'UPDATED AT', '2019-11-25 00:11:58'),
(108, 'a@gmail.com', 'REGISTERED AT', '2019-11-24 23:56:15'),
(107, 'abhiram132@gmail.com', 'REGISTERED AT', '2019-11-24 23:54:43'),
(106, 'sb@gmail.com', 'DELETED AT', '2019-11-24 23:52:47'),
(105, 'sb@gmail.com', 'REGISTERED AT', '2019-11-24 23:52:14'),
(104, 'sb@gmail.com', 'REGISTERED AT', '2019-11-24 23:52:11'),
(103, 'manoj@gmail.com', 'REGISTERED AT', '2019-11-24 23:37:03'),
(102, 'sb@gmail.com', 'REGISTERED AT', '2019-11-24 20:56:49'),
(101, 'sb@gmail.com', 'REGISTERED AT', '2019-11-24 20:56:35'),
(100, 'ashish@gmail.com', 'DELETED AT', '2019-11-24 20:36:51'),
(99, 'ashish@gmail.com', 'UPDATED AT', '2019-11-24 20:36:22'),
(98, 'ashish@gmail.com', 'UPDATED AT', '2019-11-24 20:35:41'),
(97, 'dhruti139@gmail.com', 'REGISTERED AT', '2019-11-24 20:31:09'),
(96, 'ashi@gmail.com', 'REGISTERED AT', '2019-11-24 20:14:37'),
(95, 'shopa@gmail.com', 'DELETED AT', '2019-11-24 19:51:21'),
(94, 'shopa@gmail.com', 'REGISTERED AT', '2019-11-24 19:50:36'),
(93, 'dhruti139@gmail.com', 'DELETED AT', '2019-11-24 19:49:39'),
(92, 'dhruti139@gmail.com', 'REGISTERED AT', '2019-11-24 19:48:16'),
(91, 'manja@gmail.com', 'DELETED AT', '2019-11-24 19:47:16'),
(90, 'shop@gmail.com', 'DELETED AT', '2019-11-24 19:47:16'),
(89, 'dhruti139@gmail.com', 'DELETED AT', '2019-11-24 19:47:16'),
(88, 'kullmanja@gmail.com', 'DELETED AT', '2019-11-24 19:47:16'),
(87, 'malla@gmail.com', 'DELETED AT', '2019-11-24 19:47:16'),
(86, 'abcd@gmail.com', 'DELETED AT', '2019-11-24 19:47:16'),
(85, 'amb@gmail.com', 'REGISTERED AT', '2019-11-24 19:40:57'),
(76, 'manja@gmail.com', 'REGISTERED AT', '2019-11-22 10:35:02'),
(77, 'shop@gmail.com', 'REGISTERED AT', '2019-11-22 10:36:28'),
(78, 'mmm@gmail.com', 'REGISTERED AT', '2019-11-22 10:43:32'),
(79, 'aaa@gmail.com', 'UPDATED AT', '2019-11-22 11:00:57'),
(80, 'kallmanja@gmail.com', 'UPDATED AT', '2019-11-22 11:03:10'),
(81, 'kullmanja@gmail.com', 'UPDATED AT', '2019-11-22 11:06:00'),
(82, 'aaa@gmail.com', 'DELETED AT', '2019-11-22 11:18:15'),
(83, 'abcd@gmail.com', 'REGISTERED AT', '2019-11-22 12:28:31'),
(84, 'malla@gmail.com', 'REGISTERED AT', '2019-11-24 19:10:04');

-- --------------------------------------------------------

--
-- Table structure for table `owners`
--

DROP TABLE IF EXISTS `owners`;
CREATE TABLE IF NOT EXISTS `owners` (
  `sid` int(20) NOT NULL,
  `sname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `mid` int(20) NOT NULL,
  PRIMARY KEY (`sid`,`sname`,`email`),
  KEY `mid` (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `owners`
--

INSERT INTO `owners` (`sid`, `sname`, `email`, `password`, `mid`) VALUES
(1, 'shop aa', 'mmm@gmail.com', '123', 32),
(3, 'shpc', 'shpc@gmail.com', '123', 32),
(10, 'shop a', 's10@gmail.com', '123', 46),
(11, 'shop d', 'shopd@gmail.com', '123', 32),
(150, 'shop b', 'shopb@gmail.com', '123', 32);

--
-- Triggers `owners`
--
DROP TRIGGER IF EXISTS `delete_owners_trig`;
DELIMITER $$
CREATE TRIGGER `delete_owners_trig` BEFORE DELETE ON `owners` FOR EACH ROW INSERT INTO logs VALUES(null,OLD.email,'DELETED AT',NOW())
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `owners_trig`;
DELIMITER $$
CREATE TRIGGER `owners_trig` BEFORE INSERT ON `owners` FOR EACH ROW INSERT INTO logs VALUES(null,NEW.email,'REGISTERED AT',NOW())
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `update_owners_trig`;
DELIMITER $$
CREATE TRIGGER `update_owners_trig` BEFORE UPDATE ON `owners` FOR EACH ROW INSERT INTO logs VALUES(null,NEW.email,'UPDATED AT',NOW())
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `mid` int(20) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `branch` varchar(50) NOT NULL,
  PRIMARY KEY (`mid`,`email`,`branch`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`mid`, `username`, `email`, `password`, `branch`) VALUES
(15, 'amesh', 'amb@gmail.com', '123', 'gasyg'),
(32, 'manoj', 'manoj@gmail.com', '123', 'ankola'),
(46, 'dhruti', 'dhruti139@gmail.com', '123', 'navundaa'),
(23101, 'hiiiiiiii', 'haaa@gmail.com', '123', 'manglore');

--
-- Triggers `users`
--
DROP TRIGGER IF EXISTS `delete_users_trig`;
DELIMITER $$
CREATE TRIGGER `delete_users_trig` BEFORE DELETE ON `users` FOR EACH ROW INSERT INTO logs VALUES(null,OLD.email,'DELETED AT',NOW())
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `update_user_trig`;
DELIMITER $$
CREATE TRIGGER `update_user_trig` BEFORE UPDATE ON `users` FOR EACH ROW INSERT INTO logs VALUES(null,NEW.email,'UPDATED AT',NOW())
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `user_trig`;
DELIMITER $$
CREATE TRIGGER `user_trig` BEFORE INSERT ON `users` FOR EACH ROW INSERT INTO logs VALUES(null,NEW.email,'REGISTERED AT',NOW())
$$
DELIMITER ;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bidders`
--
ALTER TABLE `bidders`
  ADD CONSTRAINT `bidders_ibfk_1` FOREIGN KEY (`shopid`) REFERENCES `owners` (`sid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `bidders_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `crops` (`cid`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `fd`
--
ALTER TABLE `fd`
  ADD CONSTRAINT `fd_ibfk_1` FOREIGN KEY (`sid`) REFERENCES `owners` (`sid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fd_ibfk_2` FOREIGN KEY (`cid`) REFERENCES `crops` (`cid`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
