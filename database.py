from sqlalchemy import create_engine, Column, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

import csv

engine = create_engine('sqlite:///investor.db?check_same_thread=False')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Companies(Base):
    __tablename__ = 'companies'

    ticker = Column(String, primary_key=True)
    name = Column(String)
    sector = Column(String)


class Financial(Base):
    __tablename__ = 'financial'

    ticker = Column(String, primary_key=True)
    ebitda = Column(Float)
    sales = Column(Float)
    net_profit = Column(Float)
    market_price = Column(Float)
    net_debt = Column(Float)
    assets = Column(Float)
    equity = Column(Float)
    cash_equivalents = Column(Float)
    liabilities = Column(Float)


class DBHandler:
    def __init__(self):
        self.session = Session()
        Base.metadata.create_all(engine)
        self.load_dataset('test/companies.csv', 'companies')
        self.load_dataset('test/financial.csv', 'financial')
        # print("Database created successfully!")

    def load_dataset(self, csv_filepath, tablename):
        with open(csv_filepath, newline='') as dataset:
            file_reader = csv.DictReader(dataset, delimiter=",")
            try:
                for line in file_reader:
                    line = {k: None if v == "" else v for k, v in line.items()}
                    self.add_data(line, tablename)
            except IntegrityError:
                self.session.rollback()

    def add_data(self, data, tablename):
        if tablename == 'companies':
            new_data = Companies(
                ticker=data['ticker'],
                name=data['name'],
                sector=data['sector']
            )
        elif tablename == 'financial':
            new_data = Financial(
                ticker=data['ticker'],
                ebitda=data['ebitda'],
                sales=data['sales'],
                net_profit=data['net_profit'],
                market_price=data['market_price'],
                net_debt=data['net_debt'],
                assets=data['assets'],
                equity=data['equity'],
                cash_equivalents=data['cash_equivalents'],
                liabilities=data['liabilities'],
            )
        else:
            raise ValueError("Invalid table class")
        self.session.add(new_data)
        self.session.commit()

