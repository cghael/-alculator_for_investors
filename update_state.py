from state_class import State, StateClass
from database import Companies, Financial


class Update(StateClass):

    def handle(self) -> State:
        search_result = self.search_companies()

        if len(search_result) == 0:
            print("Company not found!")
            self.get_context().pop_state_back(2)
            return self.get_context().get_state()

        self.list_matching_companies(search_result)
        self.set_related_values(search_result)
        self.get_context().pop_state_back(2)
        return self.get_context().get_state()

    def search_companies(self):
        user_input = input("Enter company name:\n")
        pattern = f"%{user_input}%"
        db = self.get_context().get_db()
        query = db.session.query(Companies)
        query_results = query.filter(Companies.name.like(pattern)).all()
        return query_results

    def set_related_values(self, search_result):
        db = self.get_context().get_db()
        try:
            company_number = int(input("Enter company number:\n"))
            company = search_result[company_number]
        except ValueError:
            print("Company not found!")
        except IndexError:
            print("Company not found!")
        else:
            company = (db.session.query(Financial)
                       .filter_by(ticker=company.ticker)
                       .first())
            self.update_company(company)
            print("Company updated successfully!")

    def update_company(self, company):
        try:
            company.ebitda = float(input(
                        "Enter ebitda (in the format '987654321'):\n"
                    ))
            company.sales = float(input(
                        "Enter sales (in the format '987654321'):\n"
                    ))
            company.net_profit = float(input(
                    "Enter net profit (in the format '987654321'):\n"
                ))
            company.market_price = float(input(
                    "Enter market price (in the format '987654321'):\n"
                ))
            company.net_debt = float(input(
                    "Enter net debt (in the format '987654321'):\n"
                ))
            company.assets = float(input(
                    "Enter assets (in the format '987654321'):\n"
                ))
            company.equity = float(input(
                    "Enter equity (in the format '987654321'):\n"
                ))
            company.cash_equivalents = float(input(
                    "Enter cash equivalents (in the format '987654321'):\n"
                ))
            company.liabilities = float(input(
                    "Enter liabilities (in the format '987654321'):\n"
                ))
        except ValueError:
            print("Invalid option!")
        else:
            self.get_context().get_db().session.commit()

    @staticmethod
    def list_matching_companies(query_result):
        for i, company in enumerate(query_result):
            print(f"{i} {company.name}")
