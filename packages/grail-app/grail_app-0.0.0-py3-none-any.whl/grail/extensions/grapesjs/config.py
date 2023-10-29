import json
import flask

GRAPESJS = {
    "height": "100%",
    "showOffsets": 1,
    "noticeOnUnload": 0,
    "storageManager": False,
    "pageManager": False,  # This should be set to true
    "container": "#gjs",
    "fromElement": True,
    "plugins": [
        "grapesjs-component-code-editor",
        "grapesjs-preset-webpage",
        "grapesjs-custom-code",
        "grapesjs-project-manager",
        "grapesjs-parser-postcss",
    ],
    "pluginsOpts": {
        "gjs-preset-webpage": {},
        "gjs-project-manager": {
            "loadFirst": False,
        },
        "grapesjs-custom-code": {
            # options
        },
        "grapesjs-component-code-editor": {},
    },
    "deviceManager": {
        # Default devices
        "devices": [
            {
                "id": "desktop",
                "name": "Desktop",
                "width": "",
            },
            {
                "id": "tablet",
                "name": "Tablet",
                "width": "770px",
                "widthMedia": "992px",
            },
            {
                "id": "mobileLandscape",
                "name": "Mobile landscape",
                "width": "568px",
                "widthMedia": "768px",
            },
            {
                "id": "mobilePortrait",
                "name": "Mobile portrait",
                "width": "320px",
                "widthMedia": "480px",
            },
            {
                "id": "1600x1200",
                "name": "touchscreen",
                "width": "1600px",  # This width will be applied on the canvas frame
                # "widthMedia": '810px', # This width that will be used for the CSS media
                "height": "1200px",  # Height will be applied on the canvas frame
            },
        ]
    },
    "blockManager": {
        # appendTo: "#blocks",
        "blocks": [],
    },
}
DEFAULT_BLOCKS = []


def add_canvas(conf):
    conf["canvas"] = {
        "styles": [
            flask.url_for("appbuilder.static", filename="css/bootstrap.min.css"),
            flask.url_for("appbuilder.static", filename="css/ab.css"),
            flask.url_for(
                "appbuilder.static",
                filename="css/themes/" + flask.current_app.appbuilder.app_theme,
            ),
        ],
        "scripts": [
            "https://cdn.tailwindcss.com",
            flask.url_for("appbuilder.static", filename="js/jquery-latest.js"),
            flask.url_for("appbuilder.static", filename="select2/select2.js"),
            flask.url_for(
                "appbuilder.static", filename="datepicker/bootstrap-datepicker.js"
            ),
            flask.url_for("appbuilder.static", filename="js/bootstrap.min.js"),
            flask.url_for("appbuilder.static", filename="js/ab.js"),
        ],
    }
    return conf


def add_blocks(conf, blocks):
    for b in blocks:
        conf["blockManager"]["blocks"].append(b)
    return conf


def add_template_blocks(conf):
    from pathlib import Path

    here = Path(__file__).parent
    paths = Path(here / "templates/blocks").glob("**/*")
    files = [x for x in paths if x.is_file()]
    blocks = []
    for f in files:
        blocks.append(
            {
                "id": f.name,
                "label": f.name,
                # // Select the component once it's dropped
                "select": True,
                # You can pass components as a JSON instead of a simple HTML string,
                # in this case we also use a defined component type `image`
                "content": f.read_text(),
                "category": "Templates",
                # This triggers `active` event on dropped components and the `image`
                # reacts by opening the AssetManager
                "activate": True,
                "media": "",
                "attributes": {"class": "fa fa-barcode"},
            }
        )

    if flask.has_app_context():
        app = flask.current_app
        paths = Path(app.template_folder).glob("**/*")
        files = [x for x in paths if x.is_file() and x.name in ["games.html"]]
        for f in files:
            blocks.append(
                {
                    "id": f.name,
                    "label": f.name,
                    # // Select the component once it's dropped
                    "select": True,
                    # You can pass components as a JSON instead of a simple HTML string,
                    # in this case we also use a defined component type `image`
                    "content": [{"type": "htmx-template"}],
                    "category": "App Templates",
                    # This triggers `active` event on dropped components and the `image`
                    # reacts by opening the AssetManager
                    "activate": True,
                    "media": "",
                    "attributes": {"class": "fa fa-barcode"},
                }
            )

    return add_blocks(conf, blocks=blocks)


def add_project_data(conf, pages):
    conf["projectData"] = pages
    return conf


def add_storage_manager(conf):
    conf["storageManager"] = {
        "type": "rest-api",
        "options": {
            "remote": {
                "urlStore": flask.url_for("PagesView.store"),  # POST
                "urlLoad": flask.url_for("PagesView.all"),  # GET
                "urlDelete": flask.url_for("PagesView.remove"),  # DELETE
            }
        },
        "autosave": False,  # Store data automatically
        "autoload": False,  # Autoload stored data on init
        "stepsBeforeSave": 1,  # If autosave is enabled, indicates how many changes are necessary before the store method is triggered
    }
    conf["pageManager"] = True
    return conf


def grapesjs_config(pages=None, storage_manager=False, blocks=DEFAULT_BLOCKS):
    c = GRAPESJS
    if pages:
        add_project_data(c, pages=pages)
    if storage_manager:
        add_storage_manager(c)
    if blocks:
        add_blocks(c, blocks)

    c = add_template_blocks(c)

    c = add_canvas(c)

    return json.dumps(c, indent=2)


def init_app(app: flask.Flask):
    pass
