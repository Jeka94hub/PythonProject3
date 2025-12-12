import json
import os
from typing import List, Dict, Any

def load_transactions(relative_path: str) -> List[Dict[str, Any]]:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "data", "operations.json")
    file_path = os.path.normpath(file_path)

    if not os.path.isfile(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw = f.read().strip()
            if not raw:
                return []
            data = json.loads(raw)
    except Exception:
        return []

    return data if isinstance(data, list) else []



if __name__ == "__main__":
    data = load_transactions("../data/operation.json")
    print(data)