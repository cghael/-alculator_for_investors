from state_class import State, StateClass


class MainMenu(StateClass):

    def handle(self) -> State:
        self.display_menu()
        result = self.handle_input()
        self.get_context().push_state_stack(result)
        return result
