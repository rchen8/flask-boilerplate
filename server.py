from app import app
import os

app.run(host='localhost', port=1337, debug=True)
# app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
