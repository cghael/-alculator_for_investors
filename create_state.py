from state_class import State, StateClass


class Create(StateClass):

    def handle(self) -> State:
        data = self.input_data()
        if data is not None:
            try:
                self.write_to_db(data)
                print("Company created successfully!")
            except ValueError:
                print("Error db create_data")
        self.get_context().pop_state_back(2)
        return self.get_context().get_state()

    @staticmethod
    def input_data():
        company = {}
        try:
            company = {
                "ticker": input(
                    "Enter ticker (in the format 'MOON'):\n"
                ),
                "name": input(
                    "Enter company (in the format 'Moon Corp'):\n"
                ),
                "sector": input(
                    "Enter industries (in the format 'Technology'):\n"
                ),
                "ebitda": float(input(
                    "Enter ebitda (in the format '987654321'):\n"
                )),
                "sales": float(input(
                    "Enter sales (in the format '987654321'):\n"
                )),
                "net_profit": float(input(
                    "Enter net profit (in the format '987654321'):\n"
                )),
                "market_price": float(input(
                    "Enter market price (in the format '987654321'):\n"
                )),
                "net_debt": float(input(
                    "Enter net debt (in the format '987654321'):\n"
                )),
                "assets": float(input(
                    "Enter assets (in the format '987654321'):\n"
                )),
                "equity": float(input(
                    "Enter equity (in the format '987654321'):\n"
                )),
                "cash_equivalents": float(input(
                    "Enter cash equivalents (in the format '987654321'):\n"
                )),
                "liabilities": float(input(
                    "Enter liabilities (in the format '987654321'):\n"
                ))
            }
        except ValueError:
            print("Invalid option!")
            return None
        return company

    def write_to_db(self, data):
        db = self.get_context().get_db()
        db.add_data(data, "companies")
        db.add_data(data, "financial")
