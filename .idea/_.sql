-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 07, 2025 at 06:23 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `_`
--

-- --------------------------------------------------------

--
-- Table structure for table `challaninfo`
--

CREATE TABLE `challaninfo` (
  `Vehicle_ID` varchar(10) NOT NULL,
  `Challan_ID` char(10) NOT NULL,
  `Reason` varchar(255) NOT NULL,
  `Mode` enum('MANUAL','AUTOMATED') DEFAULT NULL,
  `Status` enum('ACTIVE','INACTIVE') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `challaninfo`
--

INSERT INTO `challaninfo` (`Vehicle_ID`, `Challan_ID`, `Reason`, `Mode`, `Status`) VALUES
('1234567890', '1111111111', 'sdghjk', 'MANUAL', 'INACTIVE'),
('1234567890', '2222222222', 'idk', 'AUTOMATED', 'ACTIVE');

-- --------------------------------------------------------

--
-- Table structure for table `challans`
--

CREATE TABLE `challans` (
  `Vehicle_ID` varchar(10) NOT NULL,
  `Driver_ID` int(10) NOT NULL,
  `Pending_Challans` int(100) NOT NULL,
  `Past_Challans` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `challans`
--

INSERT INTO `challans` (`Vehicle_ID`, `Driver_ID`, `Pending_Challans`, `Past_Challans`) VALUES
('1234567890', 1111111111, 6, 5),
('987654321', 1000000000, 7, 3);

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_details`
--

CREATE TABLE `vehicle_details` (
  `Vehicle_ID` varchar(10) NOT NULL,
  `Driver_ID` int(10) NOT NULL,
  `Driver Name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vehicle_details`
--

INSERT INTO `vehicle_details` (`Vehicle_ID`, `Driver_ID`, `Driver Name`) VALUES
('1234567890', 1111111111, 'Advik');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `challaninfo`
--
ALTER TABLE `challaninfo`
  ADD PRIMARY KEY (`Challan_ID`),
  ADD UNIQUE KEY `Challan_ID` (`Challan_ID`),
  ADD UNIQUE KEY `Reason` (`Reason`),
  ADD KEY `Vehicle_ID` (`Vehicle_ID`) USING BTREE;

--
-- Indexes for table `challans`
--
ALTER TABLE `challans`
  ADD UNIQUE KEY `Vehicle ID` (`Vehicle_ID`),
  ADD UNIQUE KEY `Driver ID` (`Driver_ID`);

--
-- Indexes for table `vehicle_details`
--
ALTER TABLE `vehicle_details`
  ADD PRIMARY KEY (`Vehicle_ID`),
  ADD UNIQUE KEY `Vehicle_ID` (`Vehicle_ID`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `challaninfo`
--
ALTER TABLE `challaninfo`
  ADD CONSTRAINT `challaninfo_ibfk_1` FOREIGN KEY (`Vehicle_ID`) REFERENCES `vehicle_details` (`Vehicle_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
