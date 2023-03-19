
def get_doubling_year(asset, interest_rate, income, income_inc_rate):

    year = 0
    flag_doubled = 0.0
    base_asset = asset

    while flag_doubled < 2.0:
        asset = asset*(1+interest_rate) + income*(1+income_inc_rate)
        year = year+1
        flag_doubled = asset/base_asset
    print(year, flag_doubled)
    return year, flag_doubled


asset = 100

while True:
    # Base case (0.05, 30)
    interest_rate = 0.05
    income_inc_rate = 0.06
    income = 30
    y1, f1 = get_doubling_year(asset, interest_rate, income, income_inc_rate)
    
    # Double interest rate (0.05->0.1)
    interest_rate = 0.1
    income_inc_rate = 0.06
    income = 30
    y2, f2 = get_doubling_year(asset, interest_rate, income, income_inc_rate)

    # Double income (30->60)
    interest_rate = 0.05
    income_inc_rate = 0.06
    income = 60
    y3, f3 = get_doubling_year(asset, interest_rate, income, income_inc_rate)

    # Compare
    print("test:", y2, y3, f2, f3)
    if y2 > y3:
        asset = asset + 1
        continue
    else:
        if f2 < f3:
            print("Doubling income is better")
            asset = asset+1
            continue
        else:
            print("Now doubling interest rate is better")
            break

print("The INCOME/ASSET THRESHOLD for doubling ASSET is: ", 30/asset)