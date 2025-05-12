from flask import Blueprint, jsonify

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello', methods=['GET'])
def hello_mcp():
    """
    Simple endpoint that returns a Hello MCP message
    ---
    responses:
      200:
        description: A hello message
        schema:
          properties:
            message:
              type: string
              description: The hello message
              example: Hello MCP
    """
    return jsonify({'message': 'Hello MCP'})
