from typing import List
import logging
import os
import json
import base64


def openConvertFile(file_paths: List[str], return_both: bool = False) -> str:
    try:
        description = {"Extension": "", "Data": None}
        with open(file_paths, "rb") as f:
            description["Extension"] = os.path.splitext(file_paths)[-1]
            description["Data"] = base64.b64encode(f.read()).decode("ascii")
            if return_both:
                return json.dumps(description), description
            else:
                return json.dumps(description)
    except Exception as e:
        logging.error(f"[openConvertFile] ERROR: {e}")
        return None


def loadConvertFile(description: str) -> None:
    try:
        if description is not None:
            if isinstance(description, str):
                description = json.loads(description)
            return description
    except Exception as e:
        logging.error(f"[loadConvertFile] ERROR: {e}")
    return None


def loadConvertOpenFile(description: dict) -> None:
    try:
        if description is not None:
            if isinstance(description, str):
                description = json.loads(description)
            tmp_file_path = os.path.join(
                os.getcwd(), "tmp", f"temp{description['Extension']}"
            )
            with open(tmp_file_path, "wb") as f:
                f.write(base64.b64decode(description["Data"]))
            os.system(tmp_file_path)
    except Exception as e:
        logging.error(f"[loadConvertFile] ERROR: {e}")


def descriptionToJson(description: dict) -> str:
    if isinstance(description, dict):
        return json.dumps(description)
    return description
