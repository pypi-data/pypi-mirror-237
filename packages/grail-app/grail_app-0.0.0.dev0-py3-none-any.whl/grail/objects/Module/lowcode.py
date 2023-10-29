from grail.codegen.fab_app import (
    SQLAColumn,
    SQLAModel,
    M2M,
    M2O,
    O2M,
    FABView,
    Module,
)

AppExtensions = SQLAModel(
    name="AppExtensions",
    description="Represents many-to-many relationship between App and Extension",
    tablename="app_extensions",
    columns=[
        SQLAColumn(
            name="app_id",
            description="The id of the app",
            datatype="integer",
            foreign_key="apps.id",
        ),
        SQLAColumn(
            name="extension_id",
            description="The id of the extension",
            datatype="integer",
            foreign_key="extensions.id",
        ),
    ],
    relationships=[
        O2M(name="extension", target="Extension", viewonly=True),
        O2M(name="app", target="App", viewonly=True),
    ],
)

AppSpec = SQLAModel(
    name="App",
    description="An app that can be launched",
    tablename="apps",
    columns=[
        SQLAColumn(name="name", description="The name of the app", datatype="string"),
        SQLAColumn(
            name="description",
            description="The description of the app",
            datatype="string",
            nullable=True,
        ),
    ],
)

ExtensionSpec = SQLAModel(
    name="Extension",
    description="A specification for an extension ",
    tablename="extensions",
    columns=[
        SQLAColumn(
            name="name", description="The name of the extension", datatype="string"
        ),
        SQLAColumn(
            name="description",
            description="The description of the extension",
            datatype="string",
        ),
    ],
    relationships=[
        M2M(
            name="apps",
            target="App",
            backref="extensions",
            secondary="app_extensions",
        ),
    ],
)


AppModules = SQLAModel(
    name="AppModules",
    description="Represents m2m relationship between App and Module",
    tablename="app_modules",
    columns=[
        SQLAColumn(
            name="app_id",
            description="The id of the app",
            datatype="integer",
            foreign_key="apps.id",
        ),
        SQLAColumn(
            name="module_id",
            description="The id of the module",
            datatype="integer",
            foreign_key="modules.id",
        ),
    ],
    relationships=[
        O2M(name="module", target="Module", viewonly=True),
        O2M(name="app", target="App", viewonly=True),
    ],
)
ModuleModels = SQLAModel(
    name="ModuleModels",
    description="Represents m2m relationship between Module and Model",
    tablename="module_models",
    columns=[
        SQLAColumn(
            name="module_id",
            description="The id of the module",
            datatype="integer",
            foreign_key="modules.id",
        ),
        SQLAColumn(
            name="model_id",
            description="The id of the model",
            datatype="integer",
            foreign_key="sqlamodels.id",
        ),
    ],
    relationships=[
        O2M(name="module", target="Module", viewonly=True),
        O2M(name="model", target="SQLAModel", viewonly=True),
    ],
)
ModuleSpec = SQLAModel(
    name="Module",
    description="A specification for a module ",
    tablename="modules",
    columns=[
        SQLAColumn(
            name="name", description="The name of the module", datatype="string"
        ),
        SQLAColumn(
            name="description",
            description="The description of the module",
            datatype="string",
        ),
    ],
    relationships=[
        M2M(
            name="apps",
            target="App",
            backref="modules",
            secondary="app_modules",
        ),
    ],
)

SQLAModelSpec = SQLAModel(
    name="SQLAModel",
    description="A specification for a sqla model ",
    tablename="sqlamodels",
    columns=[
        SQLAColumn(name="name", description="The name of the model", datatype="string"),
        SQLAColumn(
            name="description",
            description="The description of the model",
            datatype="string",
        ),
        SQLAColumn(
            name="tablename",
            description="The tablename of the model",
            datatype="string",
        ),
    ],
    relationships=[
        M2M(
            name="modules",
            target="Module",
            backref="models",
            secondary="module_models",
        ),
    ],
)


SQLAFieldSpec = SQLAModel(
    name="SQLAColumn",
    description="A specification for a sqla field ",
    tablename="sqlafields",
    columns=[
        SQLAColumn(
            name="name", description="The name of the column", datatype="string"
        ),
        SQLAColumn(
            name="description",
            description="The description of the column",
            datatype="string",
        ),
        SQLAColumn(
            name="datatype",
            datatype="string",
            nullable=False,
        ),
        SQLAColumn(
            name="model_id",
            datatype="integer",
            foreign_key="sqlamodels.id",
            nullable=False,
        ),
    ],
    relationships=[
        M2O(
            name="model",
            target="SQLAModel",
            backref="columns",
        )
    ],
)


FABViewSpec = SQLAModel(
    name="FABView",
    description="A specification for a FAB View ",
    tablename="fabviews",
    columns=[
        SQLAColumn(name="name", description="The name of the view", datatype="string"),
        SQLAColumn(
            name="description",
            description="The description of the view",
            datatype="string",
            nullable=True,
        ),
        SQLAColumn(
            name="model_id",
            datatype="integer",
            foreign_key="sqlamodels.id",
            nullable=False,
        ),
        SQLAColumn(
            name="module_id",
            datatype="integer",
            foreign_key="modules.id",
            nullable=False,
        ),
    ],
    relationships=[
        M2O(
            name="model",
            target="SQLAModel",
            backref="views",
        ),
        M2O(
            name="module",
            target="Module",
            backref="views",
        ),
    ],
)

models = [
    AppSpec,
    ExtensionSpec,
    AppExtensions,
    ModuleSpec,
    AppModules,
    SQLAModelSpec,
    SQLAFieldSpec,
    ModuleModels,
    FABViewSpec,
]

LowCode = Module(
    name="lowcode",
    models=models,
    actions=[],
    views=[
        FABView(
            name="Apps",
            actions=[
                FABView.FABAction(
                    name="launch_app",
                    title="Lauch App",
                    icon="fa-rocket",
                    multiple=False,
                )
            ],
            model=AppSpec,
            list_columns=["name", "extensions", "modules"],
            related_views=["Extensions", "Modules"],
        ),
        FABView(
            name="Extensions",
            model=ExtensionSpec,
            list_columns=["name", "description", "apps"],
        ),
        FABView(
            name="Modules",
            model=ModuleSpec,
            list_columns=["name", "description", "apps"],
            related_views=["Models"],
        ),
        FABView(
            name="Models",
            model=SQLAModelSpec,
            list_columns=["name", "description", "modules"],
            related_views=["Fields"],
        ),
        FABView(
            name="Fields",
            model=SQLAFieldSpec,
            list_columns=[
                "name",
                "description",
                "model",
                "module",
                "datatype",
                "nullable",
            ],
        ),
        FABView(
            name="Views",
            model=FABViewSpec,
            list_columns=["name", "description", "model", "module"],
        ),
    ],
)
