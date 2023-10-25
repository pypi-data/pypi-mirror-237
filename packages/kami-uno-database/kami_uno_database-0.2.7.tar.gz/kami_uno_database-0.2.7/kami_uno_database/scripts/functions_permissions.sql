USE db_uc_kami;

GRANT EXECUTE ON FUNCTION GetDiasAtraso TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetDiasPenultimaCompra TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetDiasUltimaCompra TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetDtPenultimaCompra TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetDtPrimeiraCompra TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetDtUltimaCompra TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION getDtVencimentoFeriado TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetQtdComprasSemestre TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetQtdTotalCompras TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetStatusCliente TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetTotalComprasBimestre TO 'vinicius.val'@'%';
GRANT EXECUTE ON FUNCTION GetTotalComprasSemestre TO 'vinicius.val'@'%;