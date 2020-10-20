-- CONSULTAR ITENS EM ESTOQUE/DISPONÍVEIS
SELECT pro.idProduto,
       pro.noProduto,
       pro.deProduto,
       est.qtProduto,
       pro.vrUnitario,
       est.qtProduto * pro.vrUnitario AS vrEstoque
FROM db_Mercearia_DES.tbProduto pro
INNER JOIN db_Mercearia_DES.tbEstoque est ON est.idProduto = pro.idProduto
WHERE est.stInativo = 0;
