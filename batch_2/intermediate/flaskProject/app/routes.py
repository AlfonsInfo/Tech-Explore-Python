import os

from flask import request, jsonify, Blueprint
from utils import generator

main = Blueprint('main', __name__)

@main.route("/sign-service-anyflow/sign-docs", methods=['POST'])
def sign_docs():
    # Get request data
    file_input_base64 = request.json.get('fileBase64')
    request_data = request.json.get("data")

    app_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(app_dir, "output.pdf")  # Create an output directory if it doesn't exist
    signature_jpg = os.path.join(app_dir, "static", "dummy.jpg")

    # Error handling for missing parameters
    if not all([file_input_base64, signature_jpg, output_path]):
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        signature_base64 = generator.generate_base64_qr(request_data)
        # Call the doStamp function with appropriate parameters
        result = generator.do_stamp(
            file_input_base64=file_input_base64,
            signature_base64=signature_base64,
            output_image_path=output_path
        )

        # Return success response with optional data
        return jsonify({'message': 'Document signed successfully', 'result': result}), 200
    except Exception as e:
        # Handle exceptions
        return jsonify({'error': str(e)}), 500