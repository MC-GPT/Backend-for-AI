from flask import jsonify
import base64
import requests

def street_view(area, latitude, longitude, heading):
    api_key = "AIzaSyBfIFxNGNnYqmSKRz3x-stcQoZiAyjq6T0"
    location = str(latitude) + ',' + str(longitude)
    size = "1080x560"
    url = f"https://maps.googleapis.com/maps/api/streetview?size={size}&location={location}&heading={heading}&fov=120&pitch=30&key={api_key}"

    response = requests.get(url)

    if response.status_code == 200:
        # uri too long error
        # image_data = base64.b64encode(response.content).decode('utf-8')
        response_data = {
            'area': area,
            'image': url
        }
        return response_data
    else:
        return jsonify({'error': 'Failed to fetch the image'})
