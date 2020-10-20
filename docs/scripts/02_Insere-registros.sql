-------------------------
-- INSERINDO REGISTROS --
-------------------------

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
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoItem,vrUnitario) values (1,1,1,2,.5); -- pedido 1 João, Item 1: 2 pães
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoItem,vrUnitario) values (1,2,2,1,5.50); -- pedido 1 João, Item 2: 1 coca
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoItem,vrUnitario) values (2,1,1,10,.5); -- pedido 2 Maria, Item 1: 10 pães
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoItem,vrUnitario) values (3,3,1,4,.75); -- pedido 3 Joana, Item 1: 4 chineques
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoItem,vrUnitario) values (4,1,1,5,.5); -- pedido 4 José Item 1: 5 pães
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoItem,vrUnitario) values (4,5,2,1,2.5); -- pedido 4 José Item 2: 1 queijo
insert into db_Mercearia_DES.tbPedidoItem(idPedido,idProduto,nuOrdem,qtProdutoItem,vrUnitario) values (4,6,3,1,2.5); -- pedido 4 José Item 3: 1 mortadela

commit;

