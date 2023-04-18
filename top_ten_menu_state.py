from state_class import State, StateClass
from database import Financial


class TopTenMenu(StateClass):

    def __init__(self):
        super().__init__()
        self.options_text = {
            1: "TICKER ND/EBITDA",
            2: "TICKER ROE",
            3: "TICKER ROA"
        }
        self.count_options = {
            1: self.nd_ebitda,
            2: self.roe,
            3: self.roa
        }

    def handle(self) -> State:
        self.display_menu()
        try:
            user_input = int(input())
            if user_input not in range(4):
                raise ValueError
        except ValueError:
            print("Invalid option!")
            self.get_context().push_state_stack(State.BACK)
            return State.MAIN_MENU

        db = self.get_context().get_db()
        query = db.session.query(Financial)
        companies = query.all()
        self.top_companies(companies, user_input)

        self.get_context().push_state_stack(State.BACK)
        return State.BACK

    def top_companies(self, companies, option):
        print(f"{self.options_text[option]}")
        res_dict = {}

        for line in companies:
            res = self.count_options[option](line)
            if res is None:
                continue
            res_dict[line.ticker] = res

        sorted_dict = dict(sorted(
            res_dict.items(), key=lambda x: x[1], reverse=True
        ))

        count = 0
        for item in sorted_dict.items():
            print(f"{item[0]} {item[1]}")
            count += 1
            if count >= 10:
                break

    @staticmethod
    def nd_ebitda(line):
        if line.net_debt is None or line.ebitda is None:
            return None
        return round(line.net_debt / line.ebitda, 2)

    @staticmethod
    def roe(line):
        if line.net_profit is None or line.equity is None:
            return None
        return round(line.net_profit / line.equity, 2)

    @staticmethod
    def roa(line):
        if line.net_profit is None or line.assets is None:
            return None
        return round(line.net_profit / line.assets, 2)
