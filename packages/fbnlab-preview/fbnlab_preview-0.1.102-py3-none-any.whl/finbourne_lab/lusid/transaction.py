from finbourne_lab.lusid.base import BaseLusidLab
from finbourne_lab.lusid import LusidExperiment
import numpy as np
import finbourne_lab.lusid.ensure as ensure
import shortuuid
from datetime import datetime
import pytz


class LusidTransactionLab(BaseLusidLab):
    """Lab class for lusid transaction endpoint methods.

    """
    properties_data = ensure.PropertiesData(quiet=False)
    portfolios_data = ensure.PortfolioData(quiet=False)
    instrument_data = ensure.InstrumentData(quiet=False)
    transaction_data = ensure.TxnsData(quiet=False)

    def upsert_transactions_measurement(self, **kwargs) -> LusidExperiment:
        """Make an experiment object for lusid upsert transactions' performance.

        Keyword Args:
            x_rng (Union[int, List[int]]): the range to sample when upserting x-many transactions. Given as a list
                containing two integers or a const int value. Defaults to [1, 2000].
            n_props: number of properties to create on each transaction, defaults to None
            n_portfolios: number of portfolios to upsert the transactions to, defaults to 1
            scope: scope of the transactions, defaults to f"fbnlab-test-{str(shortuuid.uuid())}"
            code_prefix: prefix for naming the transactions, defaults to "fbnlab-test-{str(shortuuid.uuid())}"

        Returns:
            LusidExperiment: the upsert transactions experiment object.
        """

        x_rng = kwargs.get('x_rng', [1, 2000])
        n_props = kwargs.get('n_props', None)
        n_portfolios = kwargs.get('n_portfolios', 1)
        scope = kwargs.get('scope', f"fbnlab-test-{str(shortuuid.uuid())}")
        code_prefix = kwargs.get('code_prefix', f"fbnlab-test-{str(shortuuid.uuid())}")
        domain = "Transaction"

        effective_date = datetime(2018, 1, 1, tzinfo=pytz.utc)
        # ensure transaction property definitions
        if n_props is not None:
            self.properties_data.ensure(n_props, scope, domain)
        # ensure portfolios
        portfolio_codes = self.portfolios_data.build_portfolio_codes(
            n_portfolios=n_portfolios,
            code_prefix=code_prefix)
        self.portfolios_data.ensure(
            scope=scope,
            portfolio_codes=portfolio_codes,
            effective_date=effective_date)
        # ensure instruments
        instrument_prefix = "fbnlab-test"
        self.instrument_data.ensure(n_insts=x_rng[1], id_prefix=instrument_prefix)
        method = self.lusid.transaction_portfolios_api.upsert_transactions

        def build(x, _n_props):
            properties = []
            if n_props is not None:
                perpetual_properties = self.properties_data.build_perpetual_properties(
                    n_props=_n_props,
                    scope=scope,
                    domain=domain
                )
                properties = {_property.key: _property for _property in perpetual_properties}
            transactions = self.transaction_data.build_transactions(
                n_transactions=x,
                instrument_identifiers={f"Instrument/default/ClientInternal": f"{instrument_prefix}_0"},
                effective_date=effective_date,
                properties=properties)

            return lambda: method(
                scope=scope,
                code=portfolio_codes[np.random.randint(n_portfolios)],
                transaction_request=transactions,
                _preload_content=False
            )

        return LusidExperiment('upsert_transactions', build, x_rng, n_props)
