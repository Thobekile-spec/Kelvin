from otree.api import *



class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    Age_options = models.IntegerField(
        choices=[[1,'18-35'], [2,'36-49'],[3,'50-60']],
        label='1.What is your age interval?',
        widget=widgets.RadioSelect,
    )

    Gender_options = models.StringField(
        choices=['Male', 'Female', 'Prefer not to answer'],
        label='2.What is your gender status?',
        widget=widgets.RadioSelect,
    )
    Expertise_options = models.StringField(
        choices=['Accountancy', 'Economics', 'Law', 'Other'],
        label='3.What is your area of expertise?',
        widget=widgets.RadioSelect,
    )
    Ethnicity_options = models.StringField(
        choices=['Black African', 'White', 'Indian/Asian', 'Colored', 'Other'],
        label='4.What is your ethnic background?',
        widget=widgets.RadioSelect,
    )

    Citizenship_options = models.StringField(
        choices=['South African', 'Non-South African', 'Other'],
        label='5.What is your country of citizenship?',
        widget=widgets.RadioSelect,
    )

    Highest_education = models.StringField(
        choices=['Undergraduate', 'Honours', 'Masters candidate', 'PhD Candidate', 'Doctoral holder'],
        label='6.What is your academic level or title?',
        widget=widgets.RadioSelect,
    )

    Marital_status = models.StringField(
        choices=['Single', 'Cohabiting', 'Married', 'Divorced', 'Widowed', 'Other'],
        label='7.What is your marital status or title?',
        widget=widgets.RadioSelect,
    )

    Mother_tongue = models.StringField(
        choices=['Xhosa', 'Zulu', 'Venda', 'White', 'Other'],
        label='8.What is your mother tongue?',
        widget=widgets.RadioSelect,

    )

    Employment_status = models.StringField(
        choices=['Employed', 'Unemployed', 'Casual', 'Contract', 'Other'],
        label='9.What is your employment status?',
        widget=widgets.RadioSelect,
    )

    Educational_field = models.StringField(
        choices=['Economics', 'Law', 'BBA', 'Science', 'MBCHB/Health'],
        label='10.What is your field of study?',
        widget=widgets.RadioSelect,
    )

    Academic_faculty = models.StringField(
        choices=['Management and Commerce', 'Law', 'Humanities', 'Health', 'Engineering and the Built Environment',
                 'Other'],
        label='11.Which faculty do you belong to?',
        widget=widgets.RadioSelect,
    )
    Friends_advice = models.IntegerField(
        choices=[[1,'Yes'], [0,'No']],
        label='12.Do you listen to your friends advice when engaging in trades?',
        widget=widgets.RadioSelect,
    )

    Return_investment = models.IntegerField(
        choices=[[1,'Yes'], [0,'No']],
        label='13. Did you make any positive returns on those investments?',
        widget=widgets.RadioSelect,
    )

    Novice_experienced = models.IntegerField(
        choices=[[1,'Yes'], [0,'No']],
        label='14.Do you consider yourself as a novice or experienced investor?',
        widget=widgets.RadioSelect,
    )
    Profession_nonprofessional = models.IntegerField(
        choices=[[1,'Yes'], [0,'No']],
        label='15.Are you a professional or a non-professional investor?',
        widget=widgets.RadioSelect,
    )

    Trade_options = models.IntegerField(
        choices=[[1,'Yes'], [0,'No']],
        label='16.Do you trade by yourself?',
        widget=widgets.RadioSelect,
    )
    Stock_appreciate = models.StringField(
        choices=['Happy', 'Not happy'],
        label='17. How do you feel when your stock value has appreciated?',
        widget=widgets.RadioSelect,
    )

    Stock_appreciation = models.StringField(
        choices=['Buy', 'Sell', 'Inact'],
        label='18.What actions do you take when you are in such a state?',
        widget=widgets.RadioSelect,
    )
    Professional_advice = models.IntegerField(
        choices=[[1,'Yes'], [0,'No']],
        label='19.Do you seek professional advice when you embark on investment decisions, and why?',
        widget=widgets.RadioSelect,
    )

    get_1 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_2 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_3 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_4 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_5 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_6 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_7 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_8 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_9 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_10 = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )

    no_1_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_1_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_2_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_2_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_3_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_3_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_4_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_4_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_5_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_5_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_6_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_6_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )
    no_7_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_7_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_8_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_8_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_9_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_9_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )
    no_10_stock_a = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_10_stock_b = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    get_1_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_2_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_3_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_4_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_5_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_6_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_7_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_8_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_9_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    get_10_pii = models.StringField(
        verbose_name="",
        choices=(
            ("Option A", ""),
            ("Option B", ""),
            ("Option C", ""),
        ),
        widget=widgets.RadioSelectHorizontal()
    )
    no_1_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_1_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_2_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_2_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_3_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_3_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_4_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_4_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_5_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_5_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_6_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_6_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )
    no_7_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_7_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_8_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_8_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_9_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_9_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )
    no_10_stock_a_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )

    no_10_stock_b_pii = models.CurrencyField(
        verbose_name="",
        min=0,
        max=100000,
    )


# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['Age_options','Gender_options', 'Expertise_options', 'Ethnicity_options',
                   'Citizenship_options', 'Highest_education', 'Marital_status', 'Mother_tongue',
                   'Employment_status','Educational_field','Academic_faculty', 'Friends_advice',
                   'Return_investment','Novice_experienced','Profession_nonprofessional',
                   'Trade_options','Stock_appreciate','Stock_appreciation', 'Professional_advice']

class samp(Page):
    form_model = 'player'
    form_fields = ["get_1", "get_2", "get_3", "get_4", "get_5", "get_6", "get_7", "get_8", "get_9", "get_10",
                       "no_1_stock_a", "no_1_stock_b",
                       "no_2_stock_a", "no_2_stock_b",
                       "no_3_stock_a", "no_3_stock_b",
                       "no_4_stock_a", "no_4_stock_b",
                       "no_5_stock_a", "no_5_stock_b",
                       "no_6_stock_a", "no_6_stock_b",
                       "no_7_stock_a", "no_7_stock_b",
                       "no_8_stock_a", "no_8_stock_b",
                       "no_9_stock_a", "no_9_stock_b",
                       "no_10_stock_a", "no_10_stock_b",
                       "get_1_pii", "get_2_pii", "get_3_pii", "get_4_pii", "get_5_pii", "get_6_pii",
                       "get_7_pii", "get_8_pii", "get_9_pii", "get_10_pii",
                       "no_1_stock_a_pii", "no_1_stock_b_pii",
                       "no_2_stock_a_pii", "no_2_stock_b_pii",
                       "no_3_stock_a_pii", "no_3_stock_b_pii",
                       "no_4_stock_a_pii", "no_4_stock_b_pii",
                       "no_5_stock_a_pii", "no_5_stock_b_pii",
                       "no_6_stock_a_pii", "no_6_stock_b_pii",
                       "no_7_stock_a_pii", "no_7_stock_b_pii",
                       "no_8_stock_a_pii", "no_8_stock_b_pii",
                       "no_9_stock_a_pii", "no_9_stock_b_pii",
                       "no_10_stock_a_pii", "no_10_stock_b_pii",
                       ]

page_sequence = [Demographics, samp]
