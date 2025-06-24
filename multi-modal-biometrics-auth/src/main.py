# main.py

from authentication.face_recognition import FaceRecognition
from authentication.voice_recognition import VoiceRecognition
from authentication.fingerprint_recognition import FingerprintRecognition

def main():
    face_recognizer = FaceRecognition()
    voice_recognizer = VoiceRecognition()
    fingerprint_recognizer = FingerprintRecognition()

    # Example of orchestrating the authentication process
    # Step 1: Face Recognition
    face_detected = face_recognizer.detect_face()
    if face_detected:
        face_recognized = face_recognizer.recognize_face()
        print(f"Face recognized: {face_recognized}")

    # Step 2: Voice Recognition
    audio_processed = voice_recognizer.process_audio()
    if audio_processed:
        voice_recognized = voice_recognizer.recognize_voice()
        print(f"Voice recognized: {voice_recognized}")

    # Step 3: Fingerprint Recognition
    fingerprint_captured = fingerprint_recognizer.capture_fingerprint()
    if fingerprint_captured:
        fingerprint_matched = fingerprint_recognizer.match_fingerprint()
        print(f"Fingerprint matched: {fingerprint_matched}")

if __name__ == "__main__":
    main()