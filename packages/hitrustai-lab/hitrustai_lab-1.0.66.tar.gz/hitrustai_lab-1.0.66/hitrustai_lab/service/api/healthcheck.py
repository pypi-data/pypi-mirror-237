import requests
from datetime import datetime
from healthcheck import HealthCheck

from ..api import encrypt_token


class DataPayload:
    Payloads = {
        'card-abnormal': {
            "diia_serial_number": "test_diia_serial_number", 
            "connector_id": "test_connector_id", 
            "institute_id": "test_institute_id", 
            "operator_id": "test_operator_id", 
            "serial_number": "unittestSN12345786789", 
            "customer_servertime": "2021-11-09 05:10:10", 
            "pan_hash": "unit_test_card_0", 
            "merchant_id": "23456", 
            "purchase_amount": "2013000", 
            "purchase_currency": "901", 
            "udid": "unit_test_udid_0", 
            "ip_country": "Taiwan", 
            "os_name": "Windows", 
            "browser_language": "zh-TW", 
            "ip_request": "192.168.100.203"
        },
        'card-testing': {
            "diia_serial_number": "test_diia_serial_number", 
            "institute_id": "I999",
            "operator_id": "O001",
            "connector_id": "8909191002",
            "serial_number": "unittestSN12345786789", 
            "udid": "1234567890123456789",
            "customer_servertime": "2021-11-20 12:59:56",
            "pan_hash": "34m4MOQAZM9/BQVpSimvaLjeYgBUxqBi6zr4SGLqg9QbJ1D82zQxtvu4YnoyA==1",
            "pan_expire": "2032",
            "merchant_id": "451615MID001",
            "card_bin": "101671****6012",
            "ip_request": "201.167.110.111",
            "ip_source": "201.167.117.111"
        }
    }

    def add_payload(self, model_name: str, payload: dict):
        self.Payloads.update({model_name: payload})

    def get(self, model_name: str, token: str, timestamp: str):
        if model_name not in self.Payloads:
            return {}
        
        now = datetime.now()
        payload = self.Payloads.get(model_name)
        payload.update({
            "diia_serial_number": f"TEST-{now}",
            "serial_number": f"TEST-{now}",
        })
        return {
            "data_version": "1.0.0",
            "mac": encrypt_token(token, timestamp),
            "timestamp": timestamp,
            "payload": payload
        }


class Healthchecker:
    def __init__(self, model_name: str, token: str):
        self.model_name = model_name
        self.TOKEN = token

    def post_v2(self):
        url = f"http://127.0.0.1:8080/model/predict/{self.model_name}/v2/api/predict"
        input_data = DataPayload().get(
            self.model_name, self.TOKEN, timestamp="20210623001910")
        
        contents = requests.post(url, json=input_data)
        if contents.status_code == 200:
            output = contents.json()
            if output['return_code'] == "4003":
                return True, "4003"
            return False, output["return_code"]
        return False, str(contents.status_code)
    
    @staticmethod
    def add_healthcheck_url(app, check_func, url: str):
        health_check = HealthCheck()
        health_check.add_check(check_func)
        app.add_url_rule(url, "healthcheck", view_func=lambda: health_check.run())
        return app