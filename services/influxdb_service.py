from typing import Union

from influxdb import InfluxDBClient


class InfluxDBService:
    database: str = "monitoring_home"

    def __init__(self):
        self.influx = InfluxDBClient(username="root", password="password")
        self.create_database()

    def create_database(self):
        self.influx.create_database(self.database)

    def write_points(self, data: Union[dict, list]):
        if isinstance(data, list):
            self.influx.write_points(data, database=self.database)
            return
        if isinstance(data, dict):
            self.influx.write_points([data], database=self.database)
            return

        return
