-- drop database db_Mercearia_DES;

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
  `vrDesconto` decimal(15,2) NOT NULL DEFAULT 0 COMMENT 'Valor de desconto no pedido',
  `vrTotal` decimal(15,2) NOT NULL COMMENT 'Valor total do pedido',
  CONSTRAINT `FK_ClientePedido` FOREIGN KEY (idCliente) REFERENCES tbCliente(idCliente)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tbProduto` (
  `idProduto` int(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `noProduto` varchar(250) NOT NULL COMMENT 'Nome do produto',
  `deProduto` varchar(500) NULL COMMENT 'Descrição do produto',
  `vrUnitario` decimal(15,2) NOT NULL COMMENT 'Valor unitário do produto',
  `dtCadastro` datetime NOT NULL COMMENT 'Data em que o produto foi cadastrado',
  `stInativo` tinyint(1) NOT NULL DEFAULT 0 COMMENT 'Situação 0 - ativo/1 - inativo'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `tbPedidoProduto` (
  `idPedidoProduto` int(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  `idPedido` int(6) UNSIGNED NOT NULL COMMENT 'FK do pedido',
  `idProduto` int(6) UNSIGNED NOT NULL COMMENT 'FK do produto',
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


