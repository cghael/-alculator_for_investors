from state_class import State, StateClass
from database import Companies


class ListAll(StateClass):

    def handle(self) -> State:
        print("COMPANY LIST")

        db = self.get_context().get_db()
        query = db.session.query(Companies).order_by(Companies.ticker.asc())
        companies = query.all()

        for line in companies:
            print(f"{line.ticker} {line.name} {line.sector}")

        self.get_context().pop_state_back(2)
        return self.get_context().get_state()
