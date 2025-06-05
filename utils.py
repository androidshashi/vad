from datetime import datetime

def get_timestamped_filename(prefix="recording", ext="wav"):
    return f"{prefix}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{ext}"
