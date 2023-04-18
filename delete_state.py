from state_class import State, StateClass
from database import Companies, Financial


class Delete(StateClass):

    def handle(self) -> State:
        search_result = self.search_companies()

        if len(search_result) == 0:
            print("Company not found!")
            self.get_context().pop_state_back(2)
            return self.get_context().get_state()

        self.list_matching_companies(search_result)
        self.delete_company(search_result)
        self.get_context().pop_state_back(2)
        return self.get_context().get_state()

    def search_companies(self):
        user_input = input("Enter company name:\n")
        pattern = f"%{user_input}%"
        db = self.get_context().get_db()
        query = db.session.query(Companies)
        query_results = query.filter(Companies.name.like(pattern)).all()
        return query_results

    def delete_company(self, search_result):
        db = self.get_context().get_db()
        try:
            company_number = int(input("Enter company number:\n"))
            company = search_result[company_number]
        except ValueError:
            print("Company not found!")
        except IndexError:
            print("Company not found!")
        else:
            db.session.delete(company)
            db.session.commit()
            print("Company deleted successfully!")

    @staticmethod
    def list_matching_companies(query_result):
        for i, company in enumerate(query_result):
            print(f"{i} {company.name}")
