import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Render provides a $PORT environment variable.
    # If it's not found (like when running locally), it defaults to 5000.
    port = int(os.environ.get("PORT", 5000))

    # host='0.0.0.0' is required for Render to detect the service
    app.run(host='0.0.0.0', port=port, debug=False)