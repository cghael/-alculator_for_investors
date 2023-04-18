from abc import ABC, abstractmethod
from enum import Enum


class State(Enum):
    EXIT = 0
    BACK = 1
    MAIN_MENU = 2
    CRUD_MENU = 3
    TOP_TEN_MENU = 4
    CREATE = 5
    READ = 6
    UPDATE = 7
    DELETE = 8
    LIST_ALL = 9
    LIST_EBITDA = 10
    LIST_ROE = 11
    LIST_ROA = 12
    STAY = 13


TRANSITIONS = {
    State.MAIN_MENU: {
        0: State.EXIT,
        1: State.CRUD_MENU,
        2: State.TOP_TEN_MENU
    },
    State.CRUD_MENU: {
        0: State.BACK,
        1: State.CREATE,
        2: State.READ,
        3: State.UPDATE,
        4: State.DELETE,
        5: State.LIST_ALL
    },
    State.TOP_TEN_MENU: {
        0: State.BACK,
        1: State.LIST_EBITDA,
        2: State.LIST_ROE,
        3: State.LIST_ROA
    }
}


MENU_DISPLAY = {
    State.EXIT: "Exit",
    State.BACK: "Back",
    State.CRUD_MENU: "CRUD operations",
    State.TOP_TEN_MENU: "Show top ten companies by criteria",
    State.CREATE: "Create a company",
    State.READ: "Read a company",
    State.UPDATE: "Update a company",
    State.DELETE: "Delete a company",
    State.LIST_ALL: "List all companies",
    State.LIST_EBITDA: "List by ND/EBITDA",
    State.LIST_ROE: "List by ROE",
    State.LIST_ROA: "List by ROA"
}


class StateClass(ABC):

    def __init__(self):
        self._context = None

    def set_context(self, context) -> None:
        self._context = context

    def get_context(self):
        return self._context

    def handle_input(self):
        user_input = None
        try:
            user_input = input()
            int_input = int(user_input)
            print("")
            return TRANSITIONS[self._context.get_state()][int_input]
        except ValueError:
            print("Invalid option!")
            return State.STAY
        except KeyError:
            print("Invalid option!")
            return State.STAY

    def display_menu(self) -> None:
        ctx = self.get_context()
        state = ctx.get_state()
        print(state.name.replace("_", " "))
        for n, t in TRANSITIONS[state].items():
            print(f"{n} {MENU_DISPLAY[t]}")
        print("Enter an option:")

    @abstractmethod
    def handle(self) -> State:
        pass
