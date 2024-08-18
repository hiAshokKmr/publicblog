# firebase_config.py
import firebase_admin
from firebase_admin import credentials, messaging
from django.conf import settings

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
firebase_admin.initialize_app(cred)

