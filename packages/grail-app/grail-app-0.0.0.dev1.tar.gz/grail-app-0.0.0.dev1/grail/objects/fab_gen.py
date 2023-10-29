from grail.codegen.fab_app import (
    FABGenerator,
    SQLAModelGenerator,
    FABViewGenerator,
    ModulesGenerator,
)

fab_gen = FABGenerator(
    modules=ModulesGenerator(
        models={
            "user": ["User", "Group"],
            # "roles": ["Role", "Permission"],
            "blog": ["Post", "Comment", "Tag", "Category"],
        },
        views={
            "user": ["UsersAdmin", "GroupAdmin"],
            # "roles": ["RoleAdmin", "PermissionAdmin"],
            "blog": ["PostAdmin", "CommentAdmin"],
        },
        actions={"blog": ["CreatePost", "EditPost", "DeletePost"]},
        models_gen=SQLAModelGenerator(mixins=["db.Model"]),
        views_gen=FABViewGenerator(),
    )
)
