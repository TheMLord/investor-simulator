import okama as ok
import matplotlib.pyplot as plt


class Portfolio:
    def __init__(self,
                 stocks: list,
                 inflation: bool,
                 first_date: str,
                 last_date: str):
        self.invest_portfolio = ok.Portfolio(
            assets=stocks,
            inflation=inflation,
            first_date=first_date,
            last_date=last_date,
            ccy="RUB"
        )

    def view_table(self):
        return self.invest_portfolio.table

    def view_risk(self, var_percent: int, cvar_percent: int):
        risk_annual = self.invest_portfolio.risk_annual
        semideviation_annual = self.invest_portfolio.semideviation_annual
        var_historic = self.invest_portfolio.get_var_historic(level=var_percent)
        cvar_historic = self.invest_portfolio.get_cvar_historic(level=cvar_percent)
        drawdowns = self.invest_portfolio.drawdowns.min()

        return (f'годовая волатильность {risk_annual}\n'
                + f'полуотклонение {semideviation_annual}\n'
                + f'исторический Value at Risk (VaR) на уровне {var_percent}% {var_historic}\n'
                + f'Conditional Value at Risk (CVaR) на уровне {cvar_percent}% {cvar_historic}\n'
                + f'минимальное значение просадки (drawdown) {drawdowns}\n')

    def view_monte_carlo_forecast(self, years: int, n: int, path_to_save: str):
        self.invest_portfolio.plot_forecast_monte_carlo(distr="norm", years=years, n=n)
        plt.savefig(path_to_save)
        plt.close()