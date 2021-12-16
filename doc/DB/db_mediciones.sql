-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 01, 2021 at 05:35 PM
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
(23, 35, '2021-11-26', '14:45:00', 17.1, 15.2, 2, NULL),
(24, 40, '2021-11-26', '14:50:00', 17.1, 15.2, 1, NULL),
(246, 60, '2021-11-26', '15:00:00', 17.1, 15.2, 1, NULL),
(247, 20, '2021-11-27', '15:04:00', 17.1, 15.2, 1, NULL),
(1777, 35, '2021-11-30', '17:00:00', 15.2, 89.23, 2, NULL);

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
-- Table structure for table `sensor`
--

CREATE TABLE `sensor` (
  `id_sensor` int(11) NOT NULL,
  `direccion_mac` varchar(40) DEFAULT NULL,
  `modelo` varchar(40) DEFAULT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sensor`
--

INSERT INTO `sensor` (`id_sensor`, `direccion_mac`, `modelo`, `id_usuario`) VALUES
(1, 'EA:86:B7:6C:64:9B', 'Pro Max V9', 1),
(2, 'EA:86:B7:6C:64:9A', 'Pro Max V9', 2);

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
  `apellidos` varchar(80) NOT NULL,
  `isAutobusero` tinyint(1) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `matricula` varchar(10) DEFAULT NULL,
  `telefono` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `mail`, `nombre`, `apellidos`, `isAutobusero`, `edad`, `matricula`, `telefono`) VALUES
(1, 'pacolopez@gmail.com', 'Paco', 'Lopez', NULL, 34, NULL, '678 047 001'),
(2, 'juancarloshr123@gmail.com', 'Juan Carlos', 'Hernandez Ramirez', NULL, 22, NULL, '678 047 687');

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
-- Indexes for table `sensor`
--
ALTER TABLE `sensor`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1778;

--
-- AUTO_INCREMENT for table `notificacion`
--
ALTER TABLE `notificacion`
  MODIFY `id_notificacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sensor`
--
ALTER TABLE `sensor`
  MODIFY `id_sensor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

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
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `mediciones`
--
ALTER TABLE `mediciones`
  ADD CONSTRAINT `mediciones_ibfk_1` FOREIGN KEY (`id_sensor`) REFERENCES `sensor` (`id_sensor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `notificacion`
--
ALTER TABLE `notificacion`
  ADD CONSTRAINT `notificacion_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `notificacion_ibfk_2` FOREIGN KEY (`id_tipoNotificacion`) REFERENCES `tipo_notificacion` (`id_tipoNotificacion`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sensor`
--
ALTER TABLE `sensor`
  ADD CONSTRAINT `sensor_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tipo_medicion`
--
ALTER TABLE `tipo_medicion`
  ADD CONSTRAINT `tipo_medicion_ibfk_1` FOREIGN KEY (`id_tipoMedicion`) REFERENCES `mediciones` (`id_tipoMedicion`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
