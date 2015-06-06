-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jun 06, 2015 at 03:07 AM
-- Server version: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `das_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE IF NOT EXISTS `department` (
  `DeptId` int(11) NOT NULL AUTO_INCREMENT,
  `DeptName` varchar(10) NOT NULL,
  PRIMARY KEY (`DeptId`),
  UNIQUE KEY `DeptId` (`DeptId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`DeptId`, `DeptName`) VALUES
(1, 'MCS'),
(2, 'IS'),
(3, 'THM'),
(4, 'BS'),
(5, 'CA'),
(6, 'PGIR'),
(7, 'SRS'),
(8, 'RH'),
(9, 'EH'),
(10, 'EC'),
(11, 'PY');

-- --------------------------------------------------------

--
-- Table structure for table `dorm`
--

CREATE TABLE IF NOT EXISTS `dorm` (
  `DormId` int(11) NOT NULL AUTO_INCREMENT,
  `DormName` varchar(30) NOT NULL,
  `DormTypeId` int(11) NOT NULL,
  `DormLocId` int(11) NOT NULL,
  `SexType` char(5) NOT NULL,
  PRIMARY KEY (`DormId`),
  UNIQUE KEY `DormId` (`DormId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=29 ;

--
-- Dumping data for table `dorm`
--

INSERT INTO `dorm` (`DormId`, `DormName`, `DormTypeId`, `DormLocId`, `SexType`) VALUES
(1, 'Feehan Hall', 3, 2, 'M'),
(2, 'Brothers Hall', 3, 2, 'M'),
(3, 'Cottage A', 2, 2, 'M'),
(4, 'Cottage B', 2, 2, 'M'),
(5, 'Cottage C', 2, 2, 'M'),
(6, 'Cottage D', 2, 2, 'M'),
(7, 'Cottage E', 2, 2, 'M'),
(8, 'Cottage F', 2, 2, 'M'),
(9, 'Cottage G', 2, 2, 'M'),
(10, 'Unit 4', 1, 2, 'M'),
(11, 'Unit 5', 1, 2, 'M'),
(12, 'Clair Hall', 3, 2, 'F'),
(13, 'Edith Hall', 3, 2, 'F'),
(14, 'Cottage Marylinda', 2, 2, 'F'),
(15, 'Cottage Patronia ', 2, 2, 'F'),
(16, 'Cottage Alma', 2, 2, 'F'),
(17, 'Cottage Conelia', 2, 2, 'F'),
(18, 'Cottage Josepha', 2, 2, 'F'),
(19, 'Cottage Geno', 2, 2, 'F'),
(20, 'Unit 1', 1, 2, 'F'),
(21, 'Unit 2', 1, 2, 'F'),
(22, 'Unit 3', 1, 2, 'F'),
(23, 'Dorm 1', 3, 1, 'M'),
(24, 'Dorm 2', 3, 1, 'M'),
(25, 'Dorm 3', 3, 1, 'F'),
(26, 'Dorm 4', 3, 1, 'F'),
(27, 'Dorm 5', 3, 1, 'F'),
(28, 'Dorm 6', 3, 1, 'F');

-- --------------------------------------------------------

--
-- Table structure for table `dorm_location`
--

CREATE TABLE IF NOT EXISTS `dorm_location` (
  `DormLocId` int(11) NOT NULL AUTO_INCREMENT,
  `Location` varchar(40) NOT NULL,
  PRIMARY KEY (`DormLocId`),
  UNIQUE KEY `DormLocId` (`DormLocId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `dorm_location`
--

INSERT INTO `dorm_location` (`DormLocId`, `Location`) VALUES
(1, 'PARAMED CAMPUS'),
(2, 'MAIN CAMPUS');

-- --------------------------------------------------------

--
-- Table structure for table `dorm_types`
--

CREATE TABLE IF NOT EXISTS `dorm_types` (
  `DormTypeId` int(11) NOT NULL AUTO_INCREMENT,
  `TypeName` varchar(40) NOT NULL,
  PRIMARY KEY (`DormTypeId`),
  UNIQUE KEY `DormTypeId` (`DormTypeId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `dorm_types`
--

INSERT INTO `dorm_types` (`DormTypeId`, `TypeName`) VALUES
(1, 'UNIT'),
(2, 'COTTAGE'),
(3, 'HALL');

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE IF NOT EXISTS `faculty` (
  `FacId` int(11) NOT NULL AUTO_INCREMENT,
  `FacName` varchar(10) NOT NULL,
  PRIMARY KEY (`FacId`),
  UNIQUE KEY `FacId` (`FacId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`FacId`, `FacName`) VALUES
(1, 'FBI'),
(2, 'FASS'),
(3, 'FHS');

-- --------------------------------------------------------

--
-- Table structure for table `room_allocation`
--

CREATE TABLE IF NOT EXISTS `room_allocation` (
  `StdId` int(11) NOT NULL,
  `DormId` int(11) NOT NULL,
  `RoomNo` int(11) NOT NULL,
  PRIMARY KEY (`StdId`),
  UNIQUE KEY `StdId` (`StdId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `room_allocation`
--

INSERT INTO `room_allocation` (`StdId`, `DormId`, `RoomNo`) VALUES
(10181, 14, 26),
(10184, 7, 9),
(10193, 14, 26),
(10329, 11, 16),
(10409, 7, 9);

-- --------------------------------------------------------

--
-- Table structure for table `security_level`
--

CREATE TABLE IF NOT EXISTS `security_level` (
  `SecLevelId` int(11) NOT NULL AUTO_INCREMENT,
  `SecLevel` varchar(10) NOT NULL,
  `Description` varchar(200) NOT NULL,
  PRIMARY KEY (`SecLevelId`),
  UNIQUE KEY `SecLevelId` (`SecLevelId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `security_level`
--

INSERT INTO `security_level` (`SecLevelId`, `SecLevel`, `Description`) VALUES
(1, 'Admin', ''),
(2, 'Standard', '');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `StdId` int(11) NOT NULL,
  `Fname` varchar(30) NOT NULL,
  `Lname` varchar(30) NOT NULL,
  `Sex` char(5) NOT NULL,
  `DeptId` int(11) NOT NULL,
  `FacId` int(11) NOT NULL,
  `YearLevelId` int(11) NOT NULL,
  PRIMARY KEY (`StdId`),
  UNIQUE KEY `StdId` (`StdId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`StdId`, `Fname`, `Lname`, `Sex`, `DeptId`, `FacId`, `YearLevelId`) VALUES
(10181, 'Angela', 'Jackson', 'F', 1, 1, 4),
(10184, 'Ivan', 'Umo', 'M', 1, 1, 2),
(10193, 'Hillary', 'Davis', 'F', 10, 3, 3),
(10329, 'Daniel', 'Nelson', 'M', 1, 1, 3),
(10409, 'Donald', 'Ronald', 'M', 2, 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `user_account`
--

CREATE TABLE IF NOT EXISTS `user_account` (
  `UserId` int(11) NOT NULL AUTO_INCREMENT,
  `Fname` varchar(25) NOT NULL,
  `Lname` varchar(25) NOT NULL,
  `SecLevelId` int(11) NOT NULL,
  `Username` varchar(40) NOT NULL,
  `Password` varchar(40) NOT NULL,
  PRIMARY KEY (`UserId`),
  UNIQUE KEY `UserId` (`UserId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `user_account`
--

INSERT INTO `user_account` (`UserId`, `Fname`, `Lname`, `SecLevelId`, `Username`, `Password`) VALUES
(1, 'Daniel', 'Nelson', 2, 'dnelson', 'helloworld'),
(2, 'Stafford', 'Koki', 1, 'skoki', 'admin2015');

-- --------------------------------------------------------

--
-- Table structure for table `year_level`
--

CREATE TABLE IF NOT EXISTS `year_level` (
  `YearLevelId` int(11) NOT NULL AUTO_INCREMENT,
  `YearLevel` int(11) NOT NULL,
  PRIMARY KEY (`YearLevelId`),
  UNIQUE KEY `YearLevelId` (`YearLevelId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `year_level`
--

INSERT INTO `year_level` (`YearLevelId`, `YearLevel`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
