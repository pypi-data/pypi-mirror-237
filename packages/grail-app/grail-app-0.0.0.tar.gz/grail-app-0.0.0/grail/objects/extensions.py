from grail.codegen.fab_app import Extension, ExtensionsList

extensions = ExtensionsList(
    items=[
        Extension(
            name="appbuilder",
            requirements=[
                "flask-appbuilder",
            ],
        ),
        Extension(
            name="sqlalchemy",
            requirements=[
                "flask-sqlalchemy",
            ],
        ),
        Extension(
            name="gateway",
            requirements=[],
        ),
        Extension(
            name="gpt",
            requirements=["langchain", "openai"],
        ),
    ]
)
