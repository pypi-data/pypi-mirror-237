import sys, os

os.environ["DISABLED_WRITE"] = "1"


def run(path: str):
    from apps.admin.app import app

    client = app.test_client()
    generated = client.get(f"/generators/{path}")
    if generated.status_code == 200:
        return generated.text
    return f"Error {generated.text}"


if __name__ == "__main__":
    import sys

    print(
        run(
            'fabview?classname=FlaskApp&list_title="Your Flask Apps"&edit_columns=name,requirements_txt,app_py,settings_yaml&add_columns=name,requirements_txt,app_py,settings_yaml'
        )
    )
