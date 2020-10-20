-- CONSULTAR PEDIDO/ITENS DO PEDIDO
select ped.dtPedido as dataPedido,		
       ped.idPedido as numeroPedido,
       cli.noCliente,
       pdi.nuOrdem as itemPedido,
       pro.noProduto as nomeProduto,
       pdi.qtProdutoItem as quantidade,
       pdi.vrUnitario,
       pdi.qtProdutoItem * pdi.vrUnitario as vrTotalItem
from db_Mercearia_DES.tbProduto pro
inner join db_Mercearia_DES.tbPedidoItem pdi on pdi.idProduto = pro.idProduto
inner join db_Mercearia_DES.tbPedido ped on ped.idPedido = pdi.idPedido
inner join db_Mercearia_DES.tbCliente cli on cli.idCliente = ped.idCliente
where ped.idPedido = 1;
