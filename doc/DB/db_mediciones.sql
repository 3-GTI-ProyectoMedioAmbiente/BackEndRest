-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-01-2022 a las 18:46:53
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_mediciones`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `info_privada`
--

CREATE TABLE `info_privada` (
  `id_info` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_sensor` int(11) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `distancia_recorrida` float NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `minutos_activo` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `info_privada`
--

INSERT INTO `info_privada` (`id_info`, `id_usuario`, `id_sensor`, `telefono`, `distancia_recorrida`, `nombre`, `minutos_activo`) VALUES
(1, 23, 23, '23', 54, 'Sergi', 23),
(2, 23, 23, '23', 23, '23', 23),
(3, 23, 23, '23', 23, '23', 23),
(4, 23, 23, '23', 23, '23', 0.275984),
(5, 23, 23, '23', 23, '23', 0.147134),
(6, 23, 23, '23', 23, '23', 3.24101),
(7, 1, 1, '678 047 001', 23, 'Paquito', 4.31),
(8, 11, -1, '636363631', 23, 'Antonio', 0.12),
(9, 11, -1, '636363631', 23, 'Antonio', 0.07),
(10, 1, 1, '678 047 001', 0, 'Paquito', 0.15),
(11, 1, 1, '678 047 001', 113166, 'Paquito', 0.1),
(12, 11, 2, '636363631', 0, 'Antonio', 0.08),
(13, 11, 2, '636363631', 0, 'Antonio', 0.09),
(14, 14, -1, '321321321', 0, 'Pep', 0.08),
(15, 1, 1, '678 047 001', 642.252, 'Paquito', 0.12),
(16, 1, 1, '678 047 001', 15.3798, 'Paquito', 0.07),
(17, 1, 1, '15.379704822368678', 678, 'Paquito', 14.29),
(18, 1, 1, '678 047 001', 15.3797, 'Paquito', 15.68),
(19, 1, 1, '678 047 001', 15.3797, 'Paquito', 16.8),
(20, 1, 1, '678 047 001', 15.3797, 'Paquito', 0.18),
(21, 12, 0, '321321321', 0, 'Manuel', 0.04);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `mediciones`
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
-- Volcado de datos para la tabla `mediciones`
--

INSERT INTO `mediciones` (`id`, `medicion`, `fecha`, `hora`, `localizacion_lat`, `localizacion_lon`, `id_sensor`, `id_tipoMedicion`) VALUES
(1792, 25545.2, '2021-10-16', '15:00:00', 17.1, 15.2, 2, 4),
(1793, 25545.2, '2021-10-16', '15:00:00', 17.2, 15.3, 2, 4),
(1794, 25545.2, '2021-12-30', '15:00:00', 17.1, 15.2, 2, 4),
(1795, 25545.2, '2021-12-30', '15:00:00', 17.2, 15.3, 2, 4),
(1796, 25545.2, '2021-12-30', '15:00:00', 17.1, 15.2, 1, 4),
(1797, 25545.2, '2021-12-30', '15:00:00', 17.2, 15.3, 1, 4),
(1798, 4322, '2022-01-18', '18:34:25', 38.997, -0.166342, 1, 3),
(1799, 4498, '2022-01-18', '18:34:29', 38.997, -0.166342, 1, 3),
(1800, 4274, '2022-01-18', '18:34:33', 38.997, -0.166342, 1, 3),
(1801, 4241, '2022-01-18', '18:34:37', 38.997, -0.166342, 1, 3),
(1802, 4233, '2022-01-18', '18:34:45', 38.997, -0.166342, 1, 3),
(1803, 4261, '2022-01-18', '18:34:50', 38.997, -0.166342, 1, 3),
(1804, 4211, '2022-01-18', '18:34:54', 38.997, -0.166342, 1, 3),
(1805, 4100, '2022-01-18', '18:36:36', 38.997, -0.166342, 1, 3),
(1806, 4361, '2022-01-18', '18:36:40', 38.997, -0.166342, 1, 3),
(1807, 4133, '2022-01-18', '18:36:49', 38.997, -0.166342, 1, 3),
(1808, 3852, '2022-01-18', '18:36:53', 38.997, -0.166342, 1, 3),
(1809, 4170, '2022-01-18', '18:36:57', 38.997, -0.166342, 1, 3),
(1810, 4072, '2022-01-18', '18:37:01', 38.997, -0.166342, 1, 3),
(1811, 3965, '2022-01-18', '18:38:14', 38.997, -0.166342, 1, 3),
(1812, 3796, '2022-01-18', '18:38:19', 38.997, -0.166342, 1, 3),
(1813, 3789, '2022-01-18', '18:38:22', 38.997, -0.166342, 1, 3),
(1814, 3972, '2022-01-18', '18:38:31', 38.997, -0.166342, 1, 3),
(1815, 3996, '2022-01-18', '18:38:35', 38.997, -0.166342, 1, 3),
(1816, 3865, '2022-01-18', '18:38:39', 38.997, -0.166342, 1, 3),
(1817, 3850, '2022-01-18', '18:38:43', 38.997, -0.166342, 1, 3),
(1818, 3993, '2022-01-18', '18:38:52', 38.997, -0.166342, 1, 3),
(1819, 3841, '2022-01-18', '18:38:56', 38.997, -0.166342, 1, 3),
(1820, 3937, '2022-01-18', '18:39:00', 38.997, -0.166342, 1, 3),
(1821, 3618, '2022-01-18', '18:45:01', 38.997, -0.166342, 1, 3),
(1822, 3726, '2022-01-18', '18:45:05', 38.997, -0.166342, 1, 3),
(1823, 3539, '2022-01-18', '18:46:14', 38.997, -0.166342, 1, 3),
(1824, 3639, '2022-01-18', '18:46:18', 38.997, -0.166342, 1, 3),
(1825, 3618, '2022-01-18', '18:46:22', 38.997, -0.166342, 1, 3),
(1826, 3650, '2022-01-18', '18:46:26', 38.997, -0.166342, 1, 3),
(1827, 3557, '2022-01-18', '18:46:34', 38.997, -0.166342, 1, 3),
(1828, 3550, '2022-01-18', '18:46:38', 38.997, -0.166342, 1, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `notificacion`
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
-- Estructura de tabla para la tabla `registros_estado_nodo`
--

CREATE TABLE `registros_estado_nodo` (
  `id` int(11) NOT NULL,
  `id_sensor` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `estado` varchar(20) NOT NULL,
  `hora` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `registros_estado_nodo`
--

INSERT INTO `registros_estado_nodo` (`id`, `id_sensor`, `fecha`, `estado`, `hora`) VALUES
(8, 1, '2022-01-18', 'Conectado', '18:44:55'),
(9, 1, '2022-01-18', 'Desconectado', '18:44:55'),
(10, 1, '2022-01-18', 'Conectado', '18:44:55');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sensor`
--

CREATE TABLE `sensor` (
  `id_sensor` int(11) NOT NULL,
  `direccion_mac` varchar(40) DEFAULT NULL,
  `modelo` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `sensor`
--

INSERT INTO `sensor` (`id_sensor`, `direccion_mac`, `modelo`) VALUES
(1, 'EA:86:B7:6C:64:9B', 'Pro Max V9'),
(2, 'EA:86:B7:6C:64:9A', 'Pro Max V9');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_medicion`
--

CREATE TABLE `tipo_medicion` (
  `id_tipoMedicion` int(11) NOT NULL,
  `definicion` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tipo_medicion`
--

INSERT INTO `tipo_medicion` (`id_tipoMedicion`, `definicion`) VALUES
(3, 'NO2'),
(4, 'SO'),
(5, 'O3'),
(6, 'CO2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_notificacion`
--

CREATE TABLE `tipo_notificacion` (
  `id_tipoNotificacion` int(11) NOT NULL,
  `definicion` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL,
  `mail` varchar(40) NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `apellidos` varchar(80) NOT NULL,
  `isAutobusero` tinyint(1) DEFAULT NULL,
  `fechaNacimiento` date DEFAULT NULL,
  `matricula` varchar(10) DEFAULT NULL,
  `telefono` varchar(20) NOT NULL,
  `password` varchar(40) NOT NULL,
  `id_sensor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id_usuario`, `mail`, `nombre`, `apellidos`, `isAutobusero`, `fechaNacimiento`, `matricula`, `telefono`, `password`, `id_sensor`) VALUES
(1, 'pacolopez@gmail.com', 'Paquito', 'lopez', 0, '1980-12-09', '4645HH', '678 047 001', '123', 1),
(2, 'juancarloshr123@gmail.com', 'Juan Carlos', 'sdfsadfs', 0, '1999-01-14', '4645HH', '678 047 687', '123', NULL),
(8, 'alberto@gmail.com', 'Alberto', 'Valls', 0, '1999-02-08', 'Sin Matric', '741741741', '123', NULL),
(9, 'jc@coreanhotel.es', 'Juan Carlos', 'Hernandez Ramirez', 0, '1999-02-08', 'Sin Matric', '678047687', '123', NULL),
(11, '@mail', 'Antonio', 'Sirvent', 0, '1999-02-08', 'Sin Matric', '636363631', '123', 2),
(12, '@test', 'Manuel', 'Sempere', 0, '1999-02-08', 'Sin Matric', '321321321', '123', NULL),
(13, 'testFinal@gmail.com', 'test', 'Finalisimo', 0, '1999-02-08', 'Sin Matric', '741741741', 'hola', NULL),
(14, 'barsa@', 'Pep', 'Guardiola', 0, '2013-11-02', 'Sin Matric', '321321321', '123', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `info_privada`
--
ALTER TABLE `info_privada`
  ADD PRIMARY KEY (`id_info`);

--
-- Indices de la tabla `mediciones`
--
ALTER TABLE `mediciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_tipoMedicion` (`id_tipoMedicion`),
  ADD KEY `id_sensor` (`id_sensor`);

--
-- Indices de la tabla `notificacion`
--
ALTER TABLE `notificacion`
  ADD PRIMARY KEY (`id_notificacion`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_tipoNotificacion` (`id_tipoNotificacion`);

--
-- Indices de la tabla `registros_estado_nodo`
--
ALTER TABLE `registros_estado_nodo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `sensor`
--
ALTER TABLE `sensor`
  ADD PRIMARY KEY (`id_sensor`);

--
-- Indices de la tabla `tipo_medicion`
--
ALTER TABLE `tipo_medicion`
  ADD PRIMARY KEY (`id_tipoMedicion`);

--
-- Indices de la tabla `tipo_notificacion`
--
ALTER TABLE `tipo_notificacion`
  ADD PRIMARY KEY (`id_tipoNotificacion`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `fk_sensor` (`id_sensor`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `info_privada`
--
ALTER TABLE `info_privada`
  MODIFY `id_info` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `mediciones`
--
ALTER TABLE `mediciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1829;

--
-- AUTO_INCREMENT de la tabla `notificacion`
--
ALTER TABLE `notificacion`
  MODIFY `id_notificacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `registros_estado_nodo`
--
ALTER TABLE `registros_estado_nodo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `sensor`
--
ALTER TABLE `sensor`
  MODIFY `id_sensor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipo_medicion`
--
ALTER TABLE `tipo_medicion`
  MODIFY `id_tipoMedicion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `tipo_notificacion`
--
ALTER TABLE `tipo_notificacion`
  MODIFY `id_tipoNotificacion` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `mediciones`
--
ALTER TABLE `mediciones`
  ADD CONSTRAINT `mediciones_ibfk_1` FOREIGN KEY (`id_sensor`) REFERENCES `sensor` (`id_sensor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `notificacion`
--
ALTER TABLE `notificacion`
  ADD CONSTRAINT `notificacion_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `notificacion_ibfk_2` FOREIGN KEY (`id_tipoNotificacion`) REFERENCES `tipo_notificacion` (`id_tipoNotificacion`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `fk_sensor` FOREIGN KEY (`id_sensor`) REFERENCES `sensor` (`id_sensor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
