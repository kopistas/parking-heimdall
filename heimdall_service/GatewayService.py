from flask import Flask, jsonify
from VisionServiceRuntime import  VisionServiceRuntime
from DescriptionService import DescriptionService

class Response:
    def __init__(self, message, numberOfFreePlaces):
        self.message = message
        self.numberOfFreePlaces = numberOfFreePlaces

    def to_dict(self):
        return {'message': self.message,
                'numberOfFreePlaces': self.numberOfFreePlaces}

class GatewayService:
    def __init__(self, vision_service: VisionServiceRuntime, description_service: DescriptionService):
        self.app = Flask(__name__)
        self.vision_service = vision_service
        self.description_service = description_service
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/status', methods=['GET'])
        def get_status():
            current_result = self.vision_service.result
            if current_result == None:
                return Response('Нет данных о парковочных местах', -1)
            description = self.description_service.generate_description(current_result.empty_count)
            response = Response(description, current_result.empty_count)
            return jsonify(response.to_dict())

    def run(self):
        self.app.run(debug=True, host='0.0.0.0', port=9981)
