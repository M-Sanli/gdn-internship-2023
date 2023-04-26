from src.app import get_avg_exchange_rate
from src.app import get_historical_max_min_avg_rates
from src.app import major_difference_between_buy_ask_rate


def test_get_avg_exchange_rate():
    result_message_success = get_avg_exchange_rate(currency="USD", date="2022-02-03")
    assert "Average Currency Rate" in list(result_message_success.keys())[0]

    result_message_fail = get_avg_exchange_rate(currency="USDs", date="2022-02-03")
    assert "NBP Not Found Error" in result_message_fail[0]["message"]


def test_get_historical_max_min_avg_rates():
    result_message_success = get_historical_max_min_avg_rates(currency="USD", N="10")
    assert len(result_message_success) == 2
    assert result_message_success["Min Average Value For USD"] < result_message_success["Max Average Value For USD"]

    result_message_fail = get_historical_max_min_avg_rates(currency="USDs", N="10")
    assert "NBP Not Found Error" in result_message_fail[0]["message"]

def test_major_difference_between_buy_ask_rate():
    result_message_success = major_difference_between_buy_ask_rate(currency="USD", N="10")
    assert len(result_message_success) == 1
    assert "Major Difference Between Buy and Ask Rate" in list(result_message_success.keys())[0]

    result_message_fail = major_difference_between_buy_ask_rate(currency="USDs", N="10")
    assert "NBP Not Found Error" in result_message_fail[0]["message"]