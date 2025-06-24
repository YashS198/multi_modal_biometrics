# Configuration settings for the multi-modal biometrics authentication application

MODEL_PATHS = {
    'face_recognition': 'path/to/face/model',
    'voice_recognition': 'path/to/voice/model',
    'fingerprint_recognition': 'path/to/fingerprint/model'
}

RECOGNITION_THRESHOLDS = {
    'face_recognition': 0.85,
    'voice_recognition': 0.80,
    'fingerprint_recognition': 0.90
}

DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_username',
    'password': 'your_password',
    'database': 'biometrics_db'
}

LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'filename': 'app.log'
}