# [[[cog gen('fabview?classname=Department&list_columns=name,employees') ]]]
"""
# Department

A part of a company.

Generated from /generators/fabview?classname=Department&list_columns=name,employees
"""
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
import flask
import flask_appbuilder

from open_alchemy import models

Department = models.Department

class DepartmentView(ModelView):
    """
    # Department
    A part of a company.
    """
    route_base = '/admin/department'

    datamodel = SQLAInterface(Department)

    related_views = None
    """
        List with ModelView classes
        Will be displayed related with this one using relationship sqlalchemy property::

            class MyView(ModelView):
                datamodel = SQLAModel(Group, db.session)
                related_views = [MyOtherRelatedView]

    """
    _related_views = None
    """ internal list with ref to instantiated view classes """
    list_title = "Department"
    """ List Title, if not configured the default is 'List ' with pretty model name """
    show_title = "Department"
    """ Show Title , if not configured the default is 'Show ' with pretty model name """
    add_title = "Department"
    """ Add Title , if not configured the default is 'Add ' with pretty model name """
    edit_title = "Department"
    """ Edit Title , if not configured the default is 'Edit ' with pretty model name """

    list_columns = ['name', 'employees']
    """
        A list of columns (or model's methods) to be displayed on the list view.
        Use it to control the order of the display
    """
    show_columns = ['id', 'name', 'employees']
    """
        A list of columns (or model's methods) to be displayed on the show view.
        Use it to control the order of the display
    """
    add_columns = ['id', 'name', 'employees']
    """
        A list of columns (or model's methods) to be displayed on the add form view.
        Use it to control the order of the display
    """
    edit_columns = ['id', 'name', 'employees']
    """
        A list of columns (or model's methods) to be displayed on the edit form view.
        Use it to control the order of the display
    """
    show_exclude_columns = None
    """
       A list of columns to exclude from the show view.
       By default all columns are included.
    """
    add_exclude_columns = None
    """
       A list of columns to exclude from the add form.
       By default all columns are included.
    """
    edit_exclude_columns = None
    """
       A list of columns to exclude from the edit form.
        By default all columns are included.
    """
    order_columns = None
    """ Allowed order columns """
    page_size = 20
    """
        Use this property to change default page size
    """
    show_fieldsets = None
    """
        show fieldsets django style [(<'TITLE'|None>, {'fields':[<F1>,<F2>,...]}),....]

        ::

            class MyView(ModelView):
                datamodel = SQLAModel(MyTable, db.session)

                show_fieldsets = [
                    ('Summary', {
                        'fields': [
                            'name',
                            'address',
                            'group'
                            ]
                        }
                    ),
                    ('Personal Info', {
                        'fields': [
                            'birthday',
                            'personal_phone'
                            ],
                        'expanded':False
                        }
                    ),
                ]

    """
    add_fieldsets = None
    """
        add fieldsets django style (look at show_fieldsets for an example)
    """
    edit_fieldsets = None
    """
        edit fieldsets django style (look at show_fieldsets for an example)
    """

    description_columns = None
    """
        Dictionary with column descriptions that will be shown on the forms::

            class MyView(ModelView):
                datamodel = SQLAModel(MyTable, db.session)

                description_columns = {
                    'name': 'your models name column',
                    'address': 'the address column'
                }
    """
    validators_columns = None
    """ Dictionary to add your own validators for forms """
    formatters_columns = None
    """ Dictionary of formatter used to format the display of columns

        formatters_columns = {'some_date_col': lambda x: x.isoformat() }
    """
    add_form_extra_fields = None
    """
        A dictionary containing column names and a WTForm
        Form fields to be added to the Add form, these fields do not
        exist on the model itself ex::

        add_form_extra_fields = {'some_col':BooleanField('Some Col', default=False)}

    """
    edit_form_extra_fields = None
    """ Dictionary to add extra fields to the Edit form using this property """

    add_form_query_rel_fields = None
    """
        Add Customized query for related fields to add form.
        Assign a dictionary where the keys are the column names of
        the related models to filter, the value for each key, is a list of lists with the
        same format as base_filter
        {
            'relation col name':
                [['Related model col', FilterClass, 'Filter Value'],...],...
        }
        Add a custom filter to form related fields::

            class ContactModelView(ModelView):
                datamodel = SQLAModel(Contact, db.session)
                add_form_query_rel_fields = {'group': [['name', FilterStartsWith, 'W']]}

    """
    edit_form_query_rel_fields = None
    """
        Add Customized query for related fields to edit form.
        Assign a dictionary where the keys are the column names of
        the related models to filter, the value for each key, is a list of lists with the
        same format as base_filter
        {
            'relation col name':
                [['Related model col', FilterClass, 'Filter Value'],...],...
        }
        Add a custom filter to form related fields::

            class ContactModelView(ModelView):
                datamodel = SQLAModel(Contact, db.session)
                edit_form_query_rel_fields = {'group':[['name',FilterStartsWith,'W']]}

    """

    add_form = None
    """ To implement your own, assign WTF form for Add """
    edit_form = None
    """ To implement your own, assign WTF form for Edit """

    list_template = "appbuilder/general/model/list.html"
    """ Your own add jinja2 template for list """
    edit_template = "appbuilder/general/model/edit.html"
    """ Your own add jinja2 template for edit """
    add_template = "appbuilder/general/model/add.html"
    """ Your own add jinja2 template for add """
    show_template = "appbuilder/general/model/show.html"
    """ Your own add jinja2 template for show """

    # list_widget = ListWidget
    # """ List widget override """
    # edit_widget = FormWidget
    # """ Edit widget override """
    # add_widget = FormWidget
    # """ Add widget override """
    # show_widget = ShowWidget
    # """ Show widget override """

    actions = None

def init_app(app:flask.Flask):
    fab : flask_appbuilder.AppBuilder = app.extensions['appbuilder']
    if not fab:
        return
    with app.app_context():
        fab.add_view(DepartmentView,'Department')


