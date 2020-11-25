from datetime import datetime, timedelta
from peewee import fn
from ..models import Pedido
from .service import Service


@Service.register
class DashboardService(Service):
    @classmethod
    def sum_last_week(cls):
        date = fn.date(Pedido.dt_pedido)
        rs = Pedido\
            .select(date.alias('date'), fn.Sum(Pedido.vr_pedido).alias("total"))\
            .where(Pedido.dt_pedido >= (datetime.now() - timedelta(days=7)))\
            .group_by(date)\
            .order_by(date)\
            .execute()
        return { e.date.strftime("%d/%m/%Y"): e.total for e in rs }

