from aiogram.dispatcher.filters.state import StatesGroup, State

TOKEN = "1779909135:AAFbQegiPKYCylIfuHXd8V-nxBrh_lC1m_I"

class MyState(StatesGroup):
    main_options = State()
    menu = State()
    shares = State()
    jobs = State()
    about = State()
    