SELECT 
  IFNULL(
    CAST(`cliente_participante`.`cod_cliente` AS CHAR charset utf8mb4), 
  '0') AS 'cod_cliente',
  IFNULL(
    CAST(`cliente_participante`.`cod_colaborador` AS CHAR charset utf8mb4), 
  '0') AS 'cod_colaborador'
FROM `cd_cliente_participante` AS `cliente_participante`
WHERE (`cliente_participante`.`cod_cliente`
  IN (
    SELECT DISTINCTROW `pedido`.`cod_cliente`
    FROM `vd_pedido` AS `pedido`
    WHERE YEAR(`pedido`.`dt_implant`) >= 2022
  )
)