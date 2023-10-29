from grail.codegen.fab_app import (
    FABView,
    SQLAColumn,
    SQLAModel,
    O2M,
    M2M,
    M2O,
    O2O,
    Module,
)

Project = SQLAModel(
    name="Project",
    description="A project that people can work on",
    tablename="projects",
    columns=[
        SQLAColumn(
            name="name", description="The name of the project", datatype="string"
        ),
    ],
)

Department = SQLAModel(
    name="Department",
    description="A specification for a department ",
    tablename="departments",
    columns=[
        SQLAColumn(
            name="name", description="The name of the department", datatype="string"
        ),
    ],
)

PersonProjects = SQLAModel(
    name="PersonProjects",
    description="Represents a many-to-many relationship between Person and Project.",
    tablename="person_projects",
    columns=[
        SQLAColumn(
            name="person_id",
            description="The id of the person",
            datatype="integer",
            foreign_key="persons.id",
        ),
        SQLAColumn(
            name="project_id",
            description="The id of the project",
            datatype="integer",
            foreign_key="projects.id",
        ),
    ],
    relationships=[
        O2M(name="person", target="Person", viewonly=True),
        O2M(name="project", target="Project", viewonly=True),
    ],
)

Person = SQLAModel(
    name="Person",
    description="A specification Person ",
    tablename="persons",
    columns=[
        SQLAColumn(
            name="name", description="The name of the person", datatype="string"
        ),
        SQLAColumn(
            name="description",
            description="The description of the person",
            datatype="string",
        ),
        SQLAColumn(
            name="department_id",
            datatype="integer",
            foreign_key="departments.id",
            nullable=False,
        ),
    ],
    relationships=[
        M2M(
            name="projects",
            target="Project",
            backref="workers",
            secondary="person_projects",
        ),
        M2O(
            name="department",
            target="Department",
            backref="employees",
        ),
    ],
)
models = [Project, Department, PersonProjects, Person]
Departments = Module(
    models=models,
    name="departments",
    views=[
        FABView(
            name="Departments",
            description="A view for managing departments",
            model=Department,
        ),
        FABView(
            name="Projects",
            description="A view for managing projects",
            model=Project,
        ),
        FABView(
            name="Persons",
            description="A view for managing persons",
            model=Person,
            related_views=["Projects"],
        ),
    ],
)
