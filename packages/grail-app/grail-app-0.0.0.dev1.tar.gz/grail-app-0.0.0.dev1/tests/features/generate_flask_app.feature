# features/user.feature
Feature: Generate a Flask App
    Scenario: Generate a flask app from a FABGenerator
        Given a new FlaskApp spec "Alice" with modules blog,persons and extensions appbuilder,sqlalchemy
        When I generate the flask app
        Then The app should have extensions appbuilder,sqlalchemy
        And The app should have models Person,Group,Post,Category,Tag,Comment

#And The app should have modules blog,users


#    Scenario Outline: Generate a flask view.
#        Given I put <thing> in a blender,
#        when I switch the blender on
#        then it should transform into <other thing>
#        Examples: Models
#            | model | mixins          | list_columns | show_columns | edit_columns |
#            | user  | Audit           | name,email   | name, email  | name         |
#            | role  | Audit           | name, users  | name, users  | name         |
#            | post  | Audit, Authored | title, body  | title, body  | title, body  |
#            | tag   |                 | name, posts  | name, posts  | name         |
#
#        Examples: Views
#            | model | mixins          | list_columns | show_columns | edit_columns |
#            | user  | Audit           | name,email   | name, email  | name         |
#            | role  | Audit           | name, users  | name, users  | name         |
#            | post  | Audit, Authored | title, body  | title, body  | title, body  |
#            | tag   |                 | name, posts  | name, posts  | name         |
#
#        Examples: Consumer Electronics
#            | thing        | other thing |
#            | iPhone       | toxic waste |
#            | Galaxy Nexus | toxic waste |
#