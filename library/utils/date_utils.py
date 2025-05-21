from datetime import datetime

def calculate_late_fee(borrow_date_str, allowed_days=7, fee_per_day=1):
    try:
        borrow_date = datetime.strptime(borrow_date_str, "%Y-%m-%d")
        current_date = datetime.today()
        delta_days = (current_date - borrow_date).days
        if delta_days > allowed_days:
            return (delta_days - allowed_days) * fee_per_day
        else:
            return 0
    except ValueError:
        print("Error parsing date.")
        return 0
