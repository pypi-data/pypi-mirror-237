from langchain.chains import LLMMathChain, LLMChain
from langchain.agents import Tool, initialize_agent
from langchain import OpenAI
from langchain import PromptTemplate, FewShotPromptTemplate
from langchain.agents import AgentType

from langchain.llms import OpenAI, Anthropic
from langchain.chat_models import ChatOpenAI

# type: ignore


class AI:
    def __init__(self, openai_key) -> None:
        self.llm = OpenAI(
            temperature=0,
            openai_api_key=openai_key,
            streaming=True,
            verbose=True,
            client=ChatOpenAI,
            max_tokens=1000,
        )

        self.tools: dict = {}
        self.verbose = True
        self.agent = None
        self.history: list = []

    def create_agent(self):
        self.agent = initialize_agent(
            tools=list(self.tools.values()),
            verbose=self.verbose,
            max_iteration=3,
            llm=self.llm,
            agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        )

    @property
    def last(self):
        return self.history[-1][1]["output"]

    def ask(self, q: str):
        if not self.agent:
            self.create_agent()
        response = self.agent(q)
        self.history.append((q, response))
        return response


def create_math_tool(ai: AI):
    llm_math = LLMMathChain(llm=ai.llm)
    ai.tools["math-tool"] = Tool(
        name="Calculator",
        func=llm_math.run,
        description="Useful for when you need to answer questions about math",
        verbose=ai.verbose,
    )


def create_model_tool(ai: AI):
    # First, create the list of few shot examples.
    examples = [
        {
            "model": "Project",
            "code": """
    class Project(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255), nullable=False)
    """,
        },
        {
            "model": "Person",
            "code": """
    class Person(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255), nullable=False)
        email = db.Column(db.String(255), nullable=True)
    """,
        },
    ]

    # Next, we specify the template to format the examples we have provided.
    # We use the `PromptTemplate` class for this.
    example_formatter_template = """
    Model: {model}
    Code: {code}\n
    """
    example_prompt = PromptTemplate(
        input_variables=["model", "code"],
        template=example_formatter_template,
    )

    # Finally, we create the `FewShotPromptTemplate` object.
    few_shot_prompt = FewShotPromptTemplate(
        # These are the examples we want to insert into the prompt.
        examples=examples,
        # This is how we want to format the examples when we insert them into the prompt.
        example_prompt=example_prompt,
        # The prefix is some text that goes before the examples in the prompt.
        # Usually, this consists of intructions.
        prefix="""You are flask-appbuilder modelview generator.  
                Always respond with just a code snippets.
                Respond only with the python code for a Flask-
                AppBuilder ModelView class.  
                Do not tell me what the code is about.
                Do not tell me what the code does.\n\n""",
        # The suffix is some text that goes after the examples in the prompt.
        # Usually, this is where the user input will go
        suffix="Model: {model}\nCode:",
        # The input variables are the variables that the overall prompt expects.
        input_variables=["model"],
        # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
        example_separator="-------",
    )

    sqlamodel_chain = LLMChain(llm=ai.llm, prompt=few_shot_prompt, output_key="code")
    sqlamodel_tool = Tool(
        name="SQLAlchemy Model Generator",
        func=sqlamodel_chain.run,
        description="Useful for when you need to generate code for a sqlalchemy model",
        verbose=ai.verbose,
    )

    ai.tools["sqlamodel_tool"] = sqlamodel_tool
    # We can now generate a prompt using the `format` method.
    # print(few_shot_prompt.format(model="Car"))


def create_model_view_tool(ai: AI):
    # First, create the list of few shot examples.
    examples = [
        {
            "model": """class Project(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255), nullable=False)""",
            "code": """
        class ProjectView(ModelView):
            datamodel = SQLAInterface(Project)
            list_columns = ['id', 'name']""",
        },
        {
            "model": """class Person(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255), nullable=False)
        email = db.Column(db.String(255), nullable=True)""",
            "code": """
        class PersonView(ModelView):
            datamodel = SQLAInterface(Person)
            list_columns = ['id', 'name','email']""",
        },
    ]

    # Next, we specify the template to format the examples we have provided.
    # We use the `PromptTemplate` class for this.
    example_formatter_template = """
    Code: {model}
    View: {code}\n
    """
    example_prompt = PromptTemplate(
        input_variables=["model", "code"],
        template=example_formatter_template,
    )

    # Finally, we create the `FewShotPromptTemplate` object.
    few_shot_prompt = FewShotPromptTemplate(
        # These are the examples we want to insert into the prompt.
        examples=examples,
        # This is how we want to format the examples when we insert them into the prompt.
        example_prompt=example_prompt,
        # The prefix is some text that goes before the examples in the prompt.
        # Usually, this consists of intructions.
        prefix="""You are flask-sqlalchemy model generator.  
                 Always respond with just a code snippets.
                Respond only with the python code for a flask-sqlalchemy model class.  
                Do not tell me what the code is about.
                Do not tell me what the code does.Show all related objects classes\n\n""",
        # The suffix is some text that goes after the examples in the prompt.
        # Usually, this is where the user input will go
        suffix="Code: {model}\nView:",
        # The input variables are the variables that the overall prompt expects.
        input_variables=["model"],
        # The example_separator is the string we will use to join the prefix, examples, and suffix together with.
        example_separator="-------",
    )

    modelview_chain = LLMChain(llm=ai.llm, prompt=few_shot_prompt, output_key="code")
    modelview_tool = Tool(
        name="FlaskAppbuilder ModelView Generator",
        func=modelview_chain.run,
        description="Generate flask-appbuilder ModelView only",
        verbose=ai.verbose,
    )
    ai.tools["modelview_tool"] = modelview_tool
    # We can now generate a prompt using the `format` method.
    # print(few_shot_prompt.format(model="Car"))


def create_ai(api_key: str) -> AI:
    ai = AI(api_key)

    create_math_tool(ai)
    create_model_tool(ai)
    create_model_view_tool(ai)

    return ai
