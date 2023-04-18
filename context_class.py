from state_class import State, StateClass
from main_menu_state import MainMenu
from crud_menu_state import CrudMenu
from top_ten_menu_state import TopTenMenu
from database import DBHandler

from create_state import Create
from read_state import Read
from update_state import Update
from delete_state import Delete
from list_all_state import ListAll


class ContextClass:

    _state_stack = [State.MAIN_MENU]
    _state = None
    _db = None

    def __init__(self):
        self._orchestrator = {
            State.MAIN_MENU: MainMenu,
            State.CRUD_MENU: CrudMenu,
            State.TOP_TEN_MENU: TopTenMenu,
            State.CREATE: Create,
            State.READ: Read,
            State.UPDATE: Update,
            State.DELETE: Delete,
            State.LIST_ALL: ListAll,
            State.BACK: self.back,
            State.EXIT: self.exit,
            State.STAY: self.stay
        }
        self.set_state()

    def get_db(self):
        return self._db

    def get_state(self) -> State:
        return self._state_stack[-1]

    def get_state_object(self) -> StateClass:
        return self._state

    def set_state(self) -> None:
        self._state = self._orchestrator[self.get_state()]()
        if self._state:
            self._state.set_context(self)

    def push_state_stack(self, state: State) -> None:
        self._state_stack.append(state)

    def pop_state_back(self, steps_back=1) -> None:
        for i in range(steps_back):
            self._state_stack.pop()

    def back(self) -> StateClass:
        self.pop_state_back(2)
        self.set_state()
        return self.get_state_object()

    def stay(self):
        self._state_stack.pop()
        return self.get_state_object()

    @staticmethod
    def exit():
        print("Have a nice day!")

    def start(self):
        print("Welcome to the Investor Program!\n")
        self._db = DBHandler()
        current_state = self.get_state()
        while current_state != State.EXIT:
            current_state = self.get_state_object().handle()
            self.set_state()
