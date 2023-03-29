from src import app
from flask_api import status

@app.route("/healthcheck", methods=['GET'])
def healthcheck():
    return {
        'success': True,
        'message': "api is running"
    }, status.HTTP_200_OK