from playhouse.shortcuts import model_to_dict
from ..models import Produto

class ProdutoService:
    def list(self) -> list[dict]:
        return [ model_to_dict(p) for p in Produto.select() ]

    def create(self, data: dict) -> dict:
        return model_to_dict(Produto.create(**data))

    def read(self, id: int) -> dict:
        return model_to_dict(Produto.get( Produto.idProduto == id ))

    def update(self, id: int, data: dict) -> dict:
        return model_to_dict(Produto.update(**data).where( Produto.idProduto == id))

    def delete(self, id: int) -> dict:
        p: Produto = Produto.get( Produto.idProduto == id )
        p.delete_instance()
        return model_to_dict(p)
