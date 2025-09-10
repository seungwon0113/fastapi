# from datetime import datetime, timedelta
#
# # def get_eta(purchase_date: datetime) -> datetime:
# #     return purchase_date + timedelta(days=2)
# #
# # def test_get_eta_2024_12_01() -> None:
# #     result = get_eta(datetime(2024,12,1))
# #     assert result == datetime(2024,12,3)
#
# DELIVERY_DAYS = 2
#
# def _is_holiday(day: datetime) -> bool:
#     "Return day of the week, where Monday == 0 ... Sunday == 6."
#     return day.weekday() > 5
#
# def get_eta(purchase_date: datetime) -> datetime:
#     current_date = purchase_date
#     remaining_days = DELIVERY_DAYS
#
#     while remaining_days > 0:
#         current_date += timedelta(days=1)
#         if not _is_holiday(current_date):
#             remaining_days -= 1
#     return current_date


'----------------------------------------------------------------------'

def add(a: int, b: int) -> int:
    return a + b

# def mul(a: int, b: int) -> int:
#     return a * b
