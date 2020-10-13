work_hours= float(input("Enter your works hours: "))
regular_tariff = float(input("Enter how much you are paid per hour: "))
overtime_tariff = 22.5
print("*"*25)

if work_hours <= 40:
    earned_money = work_hours * regular_tariff
    print("you earned: ", earned_money)
elif work_hours > 40:
    
    earned_money = 40 * regular_tariff + ( work_hours - 40)* overtime_tariff
    
    print('You earned: {} $,{}$ is regular work  $ and {}$ is overtime work'.format(earned_money,
                                                                                       40*regular_tariff,
                                                                                       (work_hours-40)*overtime_tariff))
    
    