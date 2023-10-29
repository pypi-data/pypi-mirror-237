from grail.codegen.fab_app import (
    SQLAModel,
    SQLAColumn,
    M2O,
    M2M,
    Module,
    FABView,
)

Post = SQLAModel(
    name="Post",
    tablename="post",
    columns=[
        SQLAColumn(name="title", datatype="string"),
        SQLAColumn(name="content", datatype="text"),
        SQLAColumn(name="created_at", datatype="datetime"),
        SQLAColumn(name="updated_at", datatype="datetime"),
        SQLAColumn(name="published", datatype="boolean"),
    ],
    relationships=[
        # M2O(
        #    name="author",
        #    target="persons",
        #    backref="posts",
        # ),
        # M2O(
        #    name="category",
        #    target="categories",
        #    backref="posts",
        # ),
    ],
)

Comment = SQLAModel(
    name="Comment",
    tablename="comment",
    columns=[
        SQLAColumn(name="content", datatype="text"),
        SQLAColumn(name="created_at", datatype="datetime"),
        SQLAColumn(name="updated_at", datatype="datetime"),
    ],
    relationships=[
        # M2O(
        #    name="post",
        #    target="post",
        #    backref="comments",
        # ),
        # M2O(
        #    name="author",
        #    target="person",
        #    backref="comments",
        # ),
    ],
)

Tag = SQLAModel(
    name="Tag",
    tablename="tag",
    columns=[
        SQLAColumn(name="name", datatype="string"),
    ],
)


Category = SQLAModel(
    name="Category",
    tablename="category",
    columns=[
        SQLAColumn(name="name", datatype="string"),
        SQLAColumn(name="description", datatype="text"),
    ],
)
models = [Post, Comment, Tag, Category]
Blog = Module(
    name="blog",
    description="A blooging module",
    models=models,
    actions=[],
    views=[
        FABView(
            name="Posts",
            actions=[],
            model=Post,
        ),
        FABView(
            name="Comments",
            actions=[],
            model=Comment,
        ),
    ],
)
