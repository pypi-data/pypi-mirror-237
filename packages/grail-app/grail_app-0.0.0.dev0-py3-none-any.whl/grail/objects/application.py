from grail.codegen.application import (
    Action,
    Model,
    Relationship,
    RelationshipKind,
    Attribute,
    DataType,
    DataTypeKind,
    PageModel,
    BREADPage,
    Application,
    Page,
    ActionModel,
    EventModel,
    QueryModel,
    DataModel,
)

USERS_ACTIONS: list[Action] = [
    Action(
        name="create_user",
        description="Create a user",
        parameters={"user": "User"},
        body="",
    ),
    Action(
        name="delete_user",
        description="Delete a user",
        parameters={"user": "User"},
        body="",
    ),
    Action(
        name="update_user",
        description="Update a user",
        parameters={"user": "User"},
        body="",
    ),
    Action(
        name="get_user", description="Get a user", parameters={"id": "int"}, body=""
    ),
    Action(name="get_users", description="Get all users", parameters={}, body=""),
]
APP_MODEL: DataModel[Model] = DataModel(
    models=[
        Model(
            name="Post",
            description="A blog post",
            attributes=[
                Attribute(
                    name="title",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                ),
                Attribute(
                    name="body",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                ),
            ],
        ),
        Model(
            name="Comment",
            description="A comment",
            attributes=[
                Attribute(
                    name="body",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                ),
                Attribute(
                    name="created_at",
                    datatype=DataType(kind=DataTypeKind.DATE),
                    default="NOW()",
                ),
            ],
            relationships=[
                Relationship(
                    name="author",
                    model="User",
                    description="The author of the comment",
                    kind=RelationshipKind.MANY_TO_ONE,
                ),
            ],
        ),
        Model(
            name="Tag",
            description="A tag",
            attributes=[
                Attribute(
                    name="name",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                ),
                Attribute(
                    name="value",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                ),
                Attribute(
                    name="created_at",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default="NOW()",
                ),
            ],
            relationships=[
                Relationship(
                    name="posts", model="Post", kind=RelationshipKind.MANY_TO_MANY
                )
            ],
        ),
        Model(
            name="Category",
            description="A category",
            attributes=[
                Attribute(
                    name="name",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                ),
                Attribute(
                    name="created_at",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default="NOW()",
                ),
            ],
            relationships=[
                Relationship(
                    name="posts", model="Post", kind=RelationshipKind.ONE_TO_MANY
                ),
            ],
        ),
        Model(
            name="User",
            description="A user",
            attributes=[
                Attribute(
                    name="name",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                ),
                Attribute(
                    name="email",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                ),
            ],
        ),
        Model(
            name="Group",
            description="A group",
            attributes=[],
            relationships=[
                Relationship(
                    name="users",
                    model="User",
                    kind=RelationshipKind.MANY_TO_MANY,
                    description="The users in the group",
                )
            ],
        ),
        Model(
            name="Role",
            description="A role",
            attributes=[],
            relationships=[
                Relationship(
                    name="permissions",
                    model="Permission",
                    kind=RelationshipKind.MANY_TO_MANY,
                    description="The permissions of the role",
                ),
                Relationship(
                    name="groups",
                    model="Group",
                    kind=RelationshipKind.MANY_TO_MANY,
                    description="The roles of group",
                ),
            ],
        ),
        Model(
            name="Permission",
            description="A permission",
            attributes=[
                Attribute(
                    name="object",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                ),
                Attribute(
                    name="operation",
                    datatype=DataType(kind=DataTypeKind.STRING),
                    default=None,
                    description="The operation of the permission",
                ),
            ],
        ),
    ]
)

APP_PAGES: PageModel[Page] = PageModel(
    pages=[
        BREADPage(
            name="UsersAdmin",
            model="User",
            description="CRUD View for adding users",
            browse=BREADPage.Browse(
                columns=["name", "email"],
            ),
            read=None,
            edit=BREADPage.Edit(
                columns=["name", "email"],
            ),
            add=BREADPage.Add(
                columns=["email"],
            ),
            delete=BREADPage.Delete(confirm="Are you sure you want to delete a user?"),
        ),
        BREADPage(
            name="PostsAdmin",
            model="Post",
            description="CRUD View for adding Posts",
            browse=BREADPage.Browse(
                columns=[
                    "name",
                    "title",
                ],
            ),
            read=None,
            edit=BREADPage.Edit(
                columns=["name", "email"],
            ),
            add=BREADPage.Add(
                columns=["email"],
            ),
            delete=BREADPage.Delete(
                confirm="Are you sure you want to delete this post?"
            ),
        ),
    ]
)
my_app = Application(
    name="myapp",
    datamodel=APP_MODEL,
    pagemodel=APP_PAGES,
    actionmodel=ActionModel(actions=[]),
    eventmodel=EventModel(events=[]),
    querymodel=QueryModel(queries=[]),
)
