drop database db_Mercearia_DES;

create database db_Mercearia_DES;

use db_Mercearia_DES;

CREATE TABLE `tbCliente` (
  `idCliente` int(5) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `noCliente` varchar(150) NOT NULL COMMENT 'Nome do cliente',
  `nuCPF` varchar(11) NOT NULL COMMENT 'Número do CPF do cliente',
  `deEmail` varchar(150) NOT NULL COMMENT 'Email do cliente',
  `dtCadastro` datetime NOT NULL COMMENT 'Data em que o cliente fez o cadastro',
  `stInativo` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Situação 0 - ativo/1 - inativo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tbPedido` (
  `idPedido` int(7) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `idCliente` int(6) UNSIGNED NOT NULL COMMENT 'FK Cliente do pedido',
  `dtPedido` datetime NOT NULL COMMENT 'Data em que o pedido é gerado',  
--  `vrDesconto` decimal(15,2) NOT NULL DEFAULT 0 COMMENT 'Valor de desconto no pedido',
  `vrTotal` decimal(15,2) NOT NULL COMMENT 'Valor total do pedido',
  CONSTRAINT `FK_ClientePedido` FOREIGN KEY (idCliente) REFERENCES tbCliente(idCliente)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tbProduto` (
  `idProduto` int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `noProduto` varchar(250) NOT NULL COMMENT 'Nome do produto',
  `deProduto` varchar(500) NULL COMMENT 'Descrição do produto',
 -- `tpProduto` varchar(500) NULL COMMENT 'Tipo do produto/categoria',
  `vrUnitario` decimal(15,2) NOT NULL COMMENT 'Valor unitário do produto',
  `dtCadastro` datetime NOT NULL COMMENT 'Data em que o produto foi cadastrado',
  `stInativo` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Situação 0 - ativo/1 - inativo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tbPedidoItem` (
  `idPedidoItem` int(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `idPedido` int(6) UNSIGNED NOT NULL COMMENT 'FK do pedido',
  `idProduto` int(6) UNSIGNED NOT NULL COMMENT 'FK do produto',
  `nuOrdem` int(3) UNSIGNED NOT NULL COMMENT 'Ordem do produto',
  `qtProdutoPedido` int(6) NOT NULL COMMENT 'Quantidade solicitada no pedido',
  CONSTRAINT `FK_PedidoProdutoPedido` FOREIGN KEY (idPedido) REFERENCES tbPedido(idPedido),
  CONSTRAINT `FK_PedidoProdutoProduto` FOREIGN KEY (idProduto) REFERENCES tbProduto(idProduto)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tbEstoque` (
  `idEstoque` int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `idProduto` int(6) UNSIGNED NOT NULL COMMENT 'FK do produto',
  `qtProduto` int(6) NOT NULL COMMENT 'Quantidade disponivel do produto',
  `stInativo` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Situação 0 - ativo/1 - inativo',
  CONSTRAINT `FK_ProdutoEstoque` FOREIGN KEY (idProduto) REFERENCES tbProduto(idProduto)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Inserindo clientes
insert into db_Mercearia_DES.tbCliente(noCliente,nuCPF,deEmail,dtCadastro) values ('João Moraes','00000000000','joaomoraes@gmail.com',sysdate());
insert into db_Mercearia_DES.tbCliente(noCliente,nuCPF,deEmail,dtCadastro) values ('Maria da Silva','00000000000','mariasilva@gmail.com',sysdate());
insert into db_Mercearia_DES.tbCliente(noCliente,nuCPF,deEmail,dtCadastro) values ('Joana Alves','00000000000','alvesjoana@gmail.com',sysdate());
insert into db_Mercearia_DES.tbCliente(noCliente,nuCPF,deEmail,dtCadastro) values ('José de Sousa','00000000000','josesousa@gmail.com',sysdate());

-- Inserindo Produtos
insert into db_Mercearia_DES.tbProduto(noProduto,deProduto,vrUnitario,dtCadastro) values ('Pão Francês','Pão de trigo',.50,sysdate());
insert into db_Mercearia_DES.tbProduto(noProduto,deProduto,vrUnitario,dtCadastro) values ('Coca-Cola 2 lt','Refrigerante Coca-Cola 2 litros',5.50,sysdate());
insert into db_Mercearia_DES.tbProduto(noProduto,deProduto,vrUnitario,dtCadastro) values ('Chineque','Pão de farofa',.75,sysdate());
insert into db_Mercearia_DES.tbProduto(noProduto,deProduto,vrUnitario,dtCadastro) values ('Presunto fatiado 100g','Presunto fatiado 100 gramas',3.50,sysdate());
insert into db_Mercearia_DES.tbProduto(noProduto,deProduto,vrUnitario,dtCadastro) values ('Queijo mussarela fatiado 100g','Queijo mussarela 100 gramas',2.50,sysdate());
insert into db_Mercearia_DES.tbProduto(noProduto,deProduto,vrUnitario,dtCadastro) values ('Mortadela fatiada 100g','Mortadela fatiada 100 gramas',2.50,sysdate());
insert into db_Mercearia_DES.tbProduto(noProduto,deProduto,vrUnitario,dtCadastro) values ('Cerveja Heineken Lata','Cerveja Heineken Lata 350 ml',4.50,sysdate());

-- Inserindo Estoque
insert into db_Mercearia_DES.tbEstoque(idProduto,qtProduto) values (1,50);
insert into db_Mercearia_DES.tbEstoque(idProduto,qtProduto) values (2,48);
insert into db_Mercearia_DES.tbEstoque(idProduto,qtProduto) values (3,50);
insert into db_Mercearia_DES.tbEstoque(idProduto,qtProduto) values (4,50);
insert into db_Mercearia_DES.tbEstoque(idProduto,qtProduto) values (5,50);
insert into db_Mercearia_DES.tbEstoque(idProduto,qtProduto) values (6,48);
insert into db_Mercearia_DES.tbEstoque(idProduto,qtProduto) values (7,48);

-- Inserindo Pedidos
insert into db_Mercearia_DES.tbPedido(idCliente,dtPedido,vrTotal) values (1,sysdate(),6.5); -- 2 pães, 1 coca
insert into db_Mercearia_DES.tbPedido(idCliente,dtPedido,vrTotal) values (2,sysdate(),5); -- 10 pães
insert into db_Mercearia_DES.tbPedido(idCliente,dtPedido,vrTotal) values (3,sysdate(),3); -- 4 chineque
insert into db_Mercearia_DES.tbPedido(idCliente,dtPedido,vrTotal) values (4,sysdate(),7.5); -- 5 pães, 1 queijo, 1 mortadela

-- Inserindo Itens do Pedido
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoPedido) values (1,1,1,2); -- pedido 1 João, Item 1: 2 pães
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoPedido) values (1,2,2,1); -- pedido 1 João, Item 2: 1 coca
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoPedido) values (2,1,1,10); -- pedido 2 Maria, Item 1: 10 pães
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoPedido) values (3,3,1,4); -- pedido 3 Joana, Item 1: 4 chineques
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoPedido) values (4,1,1,5); -- pedido 4 José Item 1: 5 pães
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoPedido) values (4,5,2,1); -- pedido 4 José Item 2: 1 queijo
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoPedido) values (4,6,3,1); -- pedido 4 José Item 3: 1 mortadela

commit;


---------------
-- Consultas --
---------------

-- CONSULTAR PEDIDO/ITENS DO PEDIDO
select ped.dtPedido as dataPedido,
       ped.idPedido as numeroPedido,
       pdi.nuOrdem as itemPedido,
       pro.noProduto as nomeProduto,
       pdi.qtProdutoPedido as quantidade,
       pro.vrUnitario,
       pdi.qtProdutoPedido * pro.vrUnitario as vrTotalItem
from tbProduto pro
inner join tbPedidoItem pdi on pdi.idProduto = pro.idProduto
inner join tbPedido ped on ped.idPedido = pdi.idPedido
inner join tbCliente cli on cli.idCliente = ped.idCliente
where ped.idPedido = 1;

-- Consultar Itens em Estoque/Disponíveis
select pro.idProduto,
       pro.noProduto,
       pro.deProduto,
       est.qtProduto,
       pro.vrUnitario,
       est.qtProduto * pro.vrUnitario as vrEstoque
from tbProduto pro 
inner join tbEstoque est on est.idProduto = pro.idProduto
where est.stInativo = 0;