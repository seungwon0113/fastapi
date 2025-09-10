# from datetime import datetime
#
from temp import add


#
#
def test_add() -> None:
    # given
    a, b = 1, 1
    # when
    result = add(a, b)
    # then
    assert result == 2

#
# def test_get_eta_2023_12_01() -> None:
#     result = get_eta(datetime(2021, 12, 1))
#     assert result == datetime(2021, 12, 3)
#
#
# def test_get_eta_2024_12_31() -> None:
#     result = get_eta(datetime(2024, 12, 31))
#     assert result == datetime(2025, 1, 2)
#
#
# def test_get_eta_2024_02_28() -> None:
#     result = get_eta(datetime(2024, 2, 28))
#     assert result == datetime(2024, 3, 1)

