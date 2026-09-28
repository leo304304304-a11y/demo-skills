import json
import sys

REQUIRED_FIELDS = {"timestamp", "actor", "action", "resource", "status"}

def validate_event(event_dict):
    missing = REQUIRED_FIELDS - set(event_dict.keys())
    if missing:
        return False, f"Missing required fields: {missing}"
    return True, "Valid event"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            data = json.load(f)
            ok, msg = validate_event(data)
            print("Status:", "OK" if ok else "FAIL", "-", msg)
