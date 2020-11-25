from flask import jsonify
from ..services import DashboardService
from .controller import Controller


class DashboardController(Controller):
    service: DashboardService = DashboardService
    
    @classmethod
    def get(self):
        return jsonify(self.service.sum_last_week())
