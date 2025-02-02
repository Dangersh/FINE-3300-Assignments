class Bond:
    def __init__(self, face_value, coupon_rate, maturity):
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.maturity = maturity
        self.coupon_payment = (face_value * coupon_rate) / 2  # Semi-annual coupons

    def calculate_price(self, market_rate):
        Semi_annual_rate = market_rate / 2  # Semi-annual rate
        Total_periods = self.maturity * 2  # Total periods
        pv_coupons = sum(self.coupon_payment / (1 + Semi_annual_rate) ** t for t in range(1, Total_periods + 1))
        pv_face_value = self.face_value / (1 + Semi_annual_rate) ** Total_periods
        return pv_coupons + pv_face_value  # Bond price

    def compute_current_yield(self, market_price):
        return (self.face_value * self.coupon_rate) / market_price  # CY formula


# User Input Section
face_value = float(input("Enter Face Value of Bond ($): "))
coupon_rate = float(input("Enter Coupon Rate (as decimal, e.g. 0.05 for 5%): "))
maturity = int(input("Enter Maturity (in years): "))
market_rate = float(input("Enter Market Interest Rate (as decimal, e.g. 0.06 for 6%): "))

# Create Bond object and calculate values
bond = Bond(face_value, coupon_rate, maturity)
market_price = bond.calculate_price(market_rate)
current_yield = bond.compute_current_yield(market_price)

print("Bond Price:",round(market_price,2))
print("Current Yield:",round(current_yield,2))