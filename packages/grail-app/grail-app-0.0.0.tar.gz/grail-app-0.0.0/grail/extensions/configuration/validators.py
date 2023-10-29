class ValueMustBe:
    def __init__(self, key, options) -> None:
        self.key = key
        self.options = options

    def __call__(self, form, field):
        options = self.options() if callable(self.options) else self.options
        if (
            "name" in form.data
            and form.data["name"] == self.key
            and field.data not in options
        ):
            raise ValueError(f"Must be one of {options}")


class MustBeAlphaNum:
    def __init__(self, key) -> None:
        self.key = key

    def __call__(self, form, field):
        if (
            "name" in form.data
            and form.data["name"] == self.key
            and not field.data.isalnum()
        ):
            raise ValueError(f"Value of {self.key} must be Alphanumeric")


class KeyMustBe:
    def __init__(self, options) -> None:
        self.options = options

    def __call__(self, form, field):
        options = self.options() if callable(self.options) else self.options
        if "name" in form.data and form.data["name"] not in options:
            raise ValueError(
                f"{form.data['name']} is not editable. Only {options} are editable"
            )
