import threading
import time

class Application:
    def __init__(self, gateway_service, vision_service):
        self.vision_service = vision_service
        self.gateway_service = gateway_service  # Assuming GatewayService is initialized appropriately

    def start_vision_service(self):
        self.vision_service_thread = threading.Thread(target=self.vision_service.start, args=(False,))
        self.vision_service_thread.start()

    def start_gateway_service(self):
        self.gateway_service.run()

    def run_app(self):
        try:
            self.start_vision_service()
            self.start_gateway_service()
        except KeyboardInterrupt:
            print('Stopping...')