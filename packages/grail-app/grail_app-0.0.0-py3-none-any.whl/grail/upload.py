import requests
import pathlib
import sys

APP_FILES = ["README.md", "requirements.txt", "app.py", "settings.yaml"]
UPLOAD_URL = "http://0.0.0.0:8000/api/flaskapp/upload_files/{id}"
LAUNCH_URL = "http://0.0.0.0:8000/api/flaskapp/launch/{id}"


def upload_app(id: int, paths: list[pathlib.Path | str]):
    r = requests.post(
        UPLOAD_URL.format(id=id),
        files=[
            ("files", (p.name, p.read_text(), "text/plain"))
            for p in paths
            if p.exists()
        ],
    )
    return (r.json(), r.status_code) if r.ok else (r.text, r.status_code)


def launch_app(id: int, paths: list[pathlib.Path | str]):
    result, status = upload_app(id, paths)
    if status == 200:
        r = requests.get(LAUNCH_URL.format(id=id))
        result, status = (r.json(), r.status_code) if r.ok else (r.text, r.status_code)
    return result, status


if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1])
    app_id = sys.argv[2]
    result, status = launch_app(app_id, [root / pathlib.Path(p) for p in APP_FILES])
    print(status, result)
