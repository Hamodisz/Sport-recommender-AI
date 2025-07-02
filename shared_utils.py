
import pyperclip
import uuid

def copy_to_clipboard(text):
    pyperclip.copy(text)

def generate_unique_url(base_url="https://sport-recommender-ai.streamlit.app", user_id=None):
    if not user_id:
        user_id = str(uuid.uuid4())
    return f"{base_url}?user={user_id}"
