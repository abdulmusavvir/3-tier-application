from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from prometheus_client import Counter, generate_latest, Gauge
import os
import mysql.connector

app = Flask(__name__)

# Enable CORS for the entire app
CORS(app)

# Database configuration
db_config = {
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', 'root'),
    'host': os.getenv('DB_HOST', '172.21.147.236'),
    'database': os.getenv('DB_NAME', 'simple_app')
}

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint'])
USER_COUNT = Gauge('user_count', 'Total number of users in the database')

@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'index.html')

# Route to get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    # Increment the request count metric
    REQUEST_COUNT.labels(method='GET', endpoint='/api/users').inc()

    # Connect to the database and fetch users
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # Update the user count metric
    USER_COUNT.set(len(users))

    cursor.close()
    conn.close()

    return jsonify(users)

# Route to add a new user
@app.route('/api/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()

    # Increment the request count metric
    REQUEST_COUNT.labels(method='POST', endpoint='/api/users').inc()

    # Close connection
    cursor.close()
    conn.close()

    return jsonify({"message": "User added successfully"}), 201

# Route to expose Prometheus metrics
@app.route('/metrics')
def metrics():
    # Expose the metrics in Prometheus format
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
