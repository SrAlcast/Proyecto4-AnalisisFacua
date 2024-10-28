--1. Precio promedio por tipo de producto y supermercado
SELECT c.nombre AS Tipo_producto, s.nombre AS Supermercado, AVG(d.precio) AS Precio_Promedio
FROM datos d
JOIN categoria c ON d.categoria_id = c.id
JOIN supermercados s ON d.supermercado_id = s.id
GROUP BY c.nombre, s.nombre
ORDER BY c.nombre, Precio_Promedio DESC;

--2. Productos con mayor variabilidad de precio
SELECT d.nombre AS Producto, s.nombre AS Supermercado, STDDEV(d.precio) AS Variabilidad_Precio
FROM datos d
JOIN supermercados s ON d.supermercado_id = s.id
GROUP BY d.nombre, s.nombre
ORDER BY Variabilidad_Precio DESC
LIMIT 20;

--3.Productos con el precio mínimo y el supermercado correspondiente
SELECT c.nombre AS Tipo_producto, s.nombre AS Supermercado, MIN(d.precio) AS Precio_Mínimo
FROM datos d
JOIN categoria c ON d.categoria_id = c.id
JOIN supermercados s ON d.supermercado_id = s.id
GROUP BY c.nombre, s.nombre
ORDER BY c.nombre, Precio_Mínimo;

--4.Frecuencia de cambios de precio por producto y supermercado
SELECT d.nombre AS Producto, s.nombre AS Supermercado, COUNT(DISTINCT d.precio) AS Frecuencia_Cambio
FROM datos d
JOIN supermercados s ON d.supermercado_id = s.id
GROUP BY d.nombre, s.nombre
ORDER BY Frecuencia_Cambio desc
LIMIT 20;

--5.Precio diario de un productos seleccionados
SELECT  d.nombre, d.fecha, s.nombre AS Supermercado, d.precio
FROM datos d
JOIN categoria c ON d.categoria_id = c.id
JOIN supermercados s ON d.supermercado_id = s.id
WHERE D.nombre = 'Aceite de girasol refinado 0,2º Hacendado 1 l.'
ORDER BY d.fecha, s.nombre;




