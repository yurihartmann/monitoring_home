from abc import ABC

from services.influxdb_service import InfluxDBService


class MonitoringABC(ABC):
    influxdb: InfluxDBService
    measurement: str

    def __init__(self, influxdb: InfluxDBService, measurement: str):
        self.influxdb = influxdb
        self.measurement = measurement

    def generate_points(self, tags: dict, fields: dict) -> dict:
        return {
            "measurement": self.measurement,
            "tags": tags,
            "fields": fields
        }

    def run(self):
        """Not Implemented"""
