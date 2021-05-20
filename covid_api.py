from covid import Covid

def covid_inf():
    covid = Covid()
    active = covid.get_total_active_cases()
    recovered = covid.get_total_recovered()
    death = covid.get_total_deaths()
    cn = "active cases : "+ str(active) + "\nrecovered cases : " + str(recovered) + "\ndeath : "+str(death) 
    return cn
