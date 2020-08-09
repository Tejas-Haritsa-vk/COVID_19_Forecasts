import time
from datetime import date
from datetime import datetime as d
from main_app_v2 import fit_model, forecast_cases
from Update_Database_v2 import update_database, forecasted_database

def auto_update():
    run = True
    while run:
        time_now = d.now().time().strftime('%H:%M')
        date_today = date.today().strftime('%d-%m-%Y')
        if time_now == '04:30':
            try:
                update_database()
                fit_model()
                forecasted_database()
                run_status = "Database Updated"
                
                with open("Database_Updates.log", "a+") as log_file:
                    log_file.write("  {} | {}    | {}\n".format(date_today, time_now, run_status))
                    log_file.write("----------------------------------------------------------------------------------------------------------------\n")
               
            except Exception as error:
                run_status = "Failed with Error: {}".format(error)
                
                with open("Database_Updates.log", "a+") as log_file:
                    log_file.write("  {} | {}    | {}\n".format(date_today, time_now, run_status))
                    log_file.write("----------------------------------------------------------------------------------------------------------------\n")
		
                time.sleep(360)
                try:
                    update_database()
                    fit_model()
                    forecasted_database()
                    run_status = "Database Updated"
                    
                    with open("Database_Updates.log", "a+") as log_file:
                        log_file.write("  {} | {}    | {}\n".format(date_today, time_now, run_status))
                        log_file.write("----------------------------------------------------------------------------------------------------------------\n")
                        
                except Exception as error:
                    run_status = "Failed with Error: {}".format(error)
                
                    with open("Database_Updates.log", "a+") as log_file:
                        log_file.write("  {} | {}    | {}\n".format(date_today, time_now, run_status))
                        log_file.write("----------------------------------------------------------------------------------------------------------------\n")
               
        else:    
#             print(date_today, time_now)
            time.sleep(60)
#             run = False
#             break
