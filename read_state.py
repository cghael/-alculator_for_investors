from state_class import State, StateClass
from database import Companies, Financial


class Read(StateClass):

    def handle(self) -> State:
        search_result = self.search_companies()

        if len(search_result) == 0:
            print("Company not found!")
            self.get_context().pop_state_back(2)
            return self.get_context().get_state()

        self.list_matching_companies(search_result)
        self.get_financial_results(search_result)
        self.get_context().pop_state_back(2)
        return self.get_context().get_state()

    def search_companies(self):
        user_input = input("Enter company name:\n")
        pattern = f"%{user_input}%"
        db = self.get_context().get_db()
        query = db.session.query(Companies)
        query_results = query.filter(Companies.name.like(pattern)).all()
        return query_results

    @staticmethod
    def list_matching_companies(query_result):
        for i, company in enumerate(query_result):
            print(f"{i} {company.name}")

    def get_financial_results(self, search_result):
        db = self.get_context().get_db()
        try:
            company_number = int(input("Enter company number:\n"))
            company = search_result[company_number]
        except ValueError:
            print("Company not found!")
        except IndexError:
            print("Company not found!")
        else:
            company_results = (db.session.query(Financial)
                               .filter_by(ticker=company.ticker)
                               .first())
            print(f"{company.ticker} {company.name}")
            self.print_financial_results(company_results)

    @staticmethod
    def print_financial_results(results):
        pe = (round(results.market_price / results.net_profit, 2)
              if results.market_price is not None and results.net_profit else None)
        print(f"P/E = {pe}")

        ps = (round(results.market_price / results.sales, 2)
              if results.market_price is not None and results.sales else None)
        print(f"P/S = {ps}")

        pb = (round(results.market_price / results.assets, 2)
              if results.market_price is not None and results.assets else None)
        print(f"P/B = {pb}")

        nd = (round(results.net_debt / results.ebitda, 2)
              if results.net_debt is not None and results.ebitda else None)
        print(f"ND/EBITDA = {nd}")

        roe = (round(results.net_profit / results.equity, 2)
               if results.net_profit is not None and results.equity else None)
        print(f"ROE = {roe}")

        roa = (round(results.net_profit / results.assets, 2)
               if results.net_profit is not None and results.assets else None)
        print(f"ROA = {roa}")

        la = (round(results.liabilities / results.assets, 2)
              if results.liabilities is not None and results.assets else None)
        print(f"L/A = {la}")

        print()

