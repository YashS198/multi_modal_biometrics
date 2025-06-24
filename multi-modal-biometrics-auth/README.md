# Multi-Modal Biometrics Authentication

This project implements a multi-modal biometric authentication system for phone authentication, utilizing various biometric methods including face recognition, voice recognition, and fingerprint recognition.

## Project Structure

```
multi-modal-biometrics-auth
├── src
│   ├── main.py                  # Entry point of the application
│   ├── authentication           # Module for biometric authentication methods
│   │   ├── __init__.py          # Package initialization
│   │   ├── face_recognition.py   # Face recognition functionalities
│   │   ├── voice_recognition.py   # Voice recognition functionalities
│   │   └── fingerprint_recognition.py # Fingerprint recognition functionalities
│   ├── utils                    # Utility functions
│   │   └── helpers.py           # Helper functions for model loading and data preprocessing
│   └── config                   # Configuration settings
│       └── settings.py          # Application settings and parameters
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd multi-modal-biometrics-auth
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

To run the application, execute the following command:
```
python src/main.py
```

## Biometric Methods Implemented

- **Face Recognition**: Utilizes facial detection and recognition algorithms to authenticate users based on their facial features.
- **Voice Recognition**: Processes audio input to recognize and authenticate users based on their voice patterns.
- **Fingerprint Recognition**: Captures and matches fingerprint data for user authentication.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.