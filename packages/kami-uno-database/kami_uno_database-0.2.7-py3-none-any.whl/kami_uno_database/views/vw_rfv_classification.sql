USE db_uc_kami;
CREATE OR REPLACE ALGORITHM = UNDEFINED VIEW vw_rfv_classification AS
SELECT DISTINCTROW
  IFNULL(CAST(cliente.cod_cliente AS CHAR charset utf8mb4), '0') AS cod_cliente,
  IFNULL(CAST(cliente.nome_cliente AS CHAR charset utf8mb4), '0') AS nome_cliente,
  IFNULL(CAST(cliente.razao_social AS CHAR charset utf8mb4), '0') AS razao_social,
  IFNULL(CAST(GetRecenciaCliente(cliente.cod_cliente) AS CHAR charset utf8mb4), '0') AS recencia,
  IFNULL(CAST(GetDiasUltimaCompra(cliente.cod_cliente) AS CHAR charset utf8mb4), '0') AS dias_ultima_compra,
  IFNULL(CAST(GetQtdComprasPeriodo(cliente.cod_cliente, DATE(CONCAT(YEAR(CURRENT_DATE()) - 1, '-01-01')), DATE(CONCAT(YEAR(CURRENT_DATE()) - 1, '-12-31'))) AS CHAR charset utf8mb4), '0') AS qtd_compras_ultimo_ano,
  IFNULL(CAST(GetFrequenciaCliente(cliente.cod_cliente) AS CHAR charset utf8mb4), '0') AS frequencia,
  IFNULL(CAST(GetTicketMedioPeriodo(cliente.cod_cliente, DATE(CONCAT(YEAR(CURRENT_DATE()) - 1, '-01-01')), DATE(CONCAT(YEAR(CURRENT_DATE()) - 1, '-12-31'))) AS CHAR charset utf8mb4), '0') AS ticket_medio
FROM
  cd_cliente AS cliente  
WHERE
  cliente.cod_cliente IN (
    SELECT DISTINCTROW nota_fiscal.cod_cliente
    FROM vw_sales_invoices AS nota_fiscal
    WHERE
      nota_fiscal.dt_emissao >= '2022-01-01'
      AND nota_fiscal.cod_empresa IN (1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16)
  )
GROUP BY
  cliente.cod_cliente;