from data_base.bd import DataBase
from models.investor import Investor
from models.portfolio import Portfolio
from models.stock import Stock


def main():
    data_base = DataBase()

    existing_investor = data_base.session.query(Investor).filter_by(login='misha').first()

    investor_stocks = data_base.session.query(Stock).filter_by(investor_id=existing_investor.id).all()

    stocks_list = [stocks.ticker for stocks in investor_stocks]
    print(investor_stocks)
    print(stocks_list)

    portf = Portfolio(
        stocks=list(set(stocks_list)),
        inflation=True,
        first_date="2022-9",
        last_date="2023-12"
    )

    print(portf.view_table())

    print("--------------")

    print(portf.view_risk(1, 5))

    print("--------------")

    portf.view_monte_carlo_forecast(1, 20, "/home/themlord/PycharmProjects/investment-simulator/graph.png")

    data_base.close_db()


if __name__ == '__main__':
    main()

#
# investor = Investor(name="Misha", login="misha", password=123)
#
# stock1 = Stock(ticker="SIBN.MOEX", price=161.5, investor=investor)
# stock2 = Stock(ticker="YNDX.MOEX", price=2210.2, investor=investor)
# stock3 = Stock(ticker="SIBN.MOEX", price=161.5, investor=investor)
#
# data_base.session.add(investor)
# data_base.session.add(stock1)
# data_base.session.add(stock2)
# data_base.session.add(stock3)
#
# data_base.session.commit()
# print(existing_investor)
# if existing_investor is not None:
#     # Использование существующего инвестора для создания новой акции
#     test_stock = Stock(ticker='GZPR', price=1500.0, investor=existing_investor)
#
#     data_base.session.add(test_stock)
#     data_base.session.commit()
#
#     investor_stocks = data_base.session.query(Stock).filter_by(investor_id=existing_investor.id).all()
#     for stock in investor_stocks:
#         print(f'Ticker: {stock.ticker}, Price: {stock.price}, Purchase Date: {stock.purchase_date}')
# else:
#     print(f'Investor with login "investor1" does not exist.')
# data_base.drop_tables()


# new_stock = Stock(ticker='AAPL', price=150.0, investor=new_investor)
# session.add(new_stock)
#
# # Сохранение изменений в базе данных
# session.commit()

# Пример запроса на вывод информации об акциях по id инвестора
# investor_id_to_query = 1
# investor_stocks = session.query(Stock).filter_by(investor_id=investor_id_to_query).all()
#
# for stock in investor_stocks:
#     print(f'Ticker: {stock.ticker}, Price: {stock.price}, Purchase Date: {stock.purchase_date}')
#
# # Закрытие сессии
# session.close()
