-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 31, 2021 at 07:02 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_mediciones`
--

-- --------------------------------------------------------

--
-- Table structure for table `mediciones`
--

CREATE TABLE `mediciones` (
  `id` int(11) NOT NULL,
  `medicion` float NOT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `localizacion_lat` float DEFAULT NULL,
  `localizacion_lon` float DEFAULT NULL,
  `id_sensor` int(11) DEFAULT NULL,
  `id_tipoMedicion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mediciones`
--

INSERT INTO `mediciones` (`id`, `medicion`, `fecha`, `hora`, `localizacion_lat`, `localizacion_lon`, `id_sensor`, `id_tipoMedicion`) VALUES
(23, 25545.2, '2021-10-16', '15:15:00', 17.1, 15.2, NULL, NULL),
(24, 58.25, '2021-10-16', '16:24:00', 17.1, 15.2, NULL, NULL),
(26, 58.25, '2021-10-16', '16:24:00', 17.1, 15.2, NULL, NULL),
(27, 25545.2, '2021-10-16', '15:15:00', 17.1, 15.2, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `notificacion`
--

CREATE TABLE `notificacion` (
  `id_notificacion` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `descripcion` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `id_tipoNotificacion` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `sesnsor`
--

CREATE TABLE `sesnsor` (
  `id_sensor` int(11) NOT NULL,
  `direccion_mac` varchar(40) DEFAULT NULL,
  `modelo` varchar(40) DEFAULT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tipo_medicion`
--

CREATE TABLE `tipo_medicion` (
  `id_tipoMedicion` int(11) NOT NULL,
  `definicion` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `tipo_notificacion`
--

CREATE TABLE `tipo_notificacion` (
  `id_tipoNotificacion` int(11) NOT NULL,
  `definicion` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `mail` varchar(40) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `apellidos` int(80) NOT NULL,
  `isAutobusero` tinyint(1) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `matricula` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `mediciones`
--
ALTER TABLE `mediciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_tipoMedicion` (`id_tipoMedicion`),
  ADD KEY `id_sensor` (`id_sensor`);

--
-- Indexes for table `notificacion`
--
ALTER TABLE `notificacion`
  ADD PRIMARY KEY (`id_notificacion`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_tipoNotificacion` (`id_tipoNotificacion`);

--
-- Indexes for table `sesnsor`
--
ALTER TABLE `sesnsor`
  ADD PRIMARY KEY (`id_sensor`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- Indexes for table `tipo_medicion`
--
ALTER TABLE `tipo_medicion`
  ADD PRIMARY KEY (`id_tipoMedicion`);

--
-- Indexes for table `tipo_notificacion`
--
ALTER TABLE `tipo_notificacion`
  ADD PRIMARY KEY (`id_tipoNotificacion`);

--
-- Indexes for table `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `mediciones`
--
ALTER TABLE `mediciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=155;

--
-- AUTO_INCREMENT for table `notificacion`
--
ALTER TABLE `notificacion`
  MODIFY `id_notificacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sesnsor`
--
ALTER TABLE `sesnsor`
  MODIFY `id_sensor` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tipo_medicion`
--
ALTER TABLE `tipo_medicion`
  MODIFY `id_tipoMedicion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `tipo_notificacion`
--
ALTER TABLE `tipo_notificacion`
  MODIFY `id_tipoNotificacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `mediciones`
--
ALTER TABLE `mediciones`
  ADD CONSTRAINT `mediciones_ibfk_1` FOREIGN KEY (`id_sensor`) REFERENCES `sesnsor` (`id_sensor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `notificacion`
--
ALTER TABLE `notificacion`
  ADD CONSTRAINT `notificacion_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `notificacion_ibfk_2` FOREIGN KEY (`id_tipoNotificacion`) REFERENCES `tipo_notificacion` (`id_tipoNotificacion`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sesnsor`
--
ALTER TABLE `sesnsor`
  ADD CONSTRAINT `sesnsor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tipo_medicion`
--
ALTER TABLE `tipo_medicion`
  ADD CONSTRAINT `tipo_medicion_ibfk_1` FOREIGN KEY (`id_tipoMedicion`) REFERENCES `mediciones` (`id_tipoMedicion`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
