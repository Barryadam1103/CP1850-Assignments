print("CELL PHONE BILL")
minutes_included = 50
text_included = 50
monthly_plan = 15.00
additional_min = 0.25
additional_text = 0.15
tax = .15
nine_one_one = .44

# Get user input
minutes = int(input("How many minutes have you used?:   "))
texts = int(input("How many texts have you sent?:   "))

if minutes <= minutes_included and texts <= text_included:
    
    add_total = round(monthly_plan + nine_one_one, 2) * .15
    final_total = round(nine_one_one + add_total + monthly_plan , 2)
    

elif minutes <= minutes_included and texts > text_included:            
    extra_texts = (texts - text_included) * 0.15
    total = (monthly_plan + extra_texts + nine_one_one) * .15
    final_total= round(monthly_plan + extra_texts + nine_one_one + total , 2)
    
elif minutes > minutes_included and texts <= text_included:
    extra_minutes = (minutes - minutes_included) * 0.25
    total =(monthly_plan + extra_minutes + nine_one_one) * .15
    final_total = round(total + nine_one_one + extra_minutes + monthly_plan, 2)

else:
    if minutes > minutes_included and texts > text_included:
        extra_minutes = (minutes - minutes_included) * 0.25
        extra_texts = (texts - text_included) * 0.15
        total = (monthly_plan + extra_texts + extra_minutes + nine_one_one) * .15
        final_total = round(monthly_plan + extra_texts + extra_minutes + nine_one_one + total, 2)
        
# Get Final Bill    
print("Your Total minutes are", final_total)


