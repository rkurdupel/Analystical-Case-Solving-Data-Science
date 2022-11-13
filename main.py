#місце для твого коду

import pandas as pd
df = pd.read_csv("DataAnalyst.csv")
print(df.info())



# --------------------------
# POSITION DEPENDS ON SALARY
# --------------------------
print(df[["Job Title", "Salary Estimate"]].head(3)) # отримати дані з стовпчика Job Title та Salary Estimate
print(df[["Job Title", "Salary Estimate"]].tail(3))
print(df[["Job Title", "Salary Estimate"]][1300:1305])  # [1300:1305] - певні рядки з файлу (csv)
#print(df.groupby(by = "Job Title")['Salary Estimate'])
# table = df.pivot_table(index = "Job Title", values = 'Salary Estimate', columns = ",)
#print(table)

#print(df["Size"].mean())

# ----------------------------
# MINIMAL REVENUE OF EMPLOYEES
# ----------------------------
def get_min_revenue(data):
    if "to" in data:
        try:
            data = data.split("to")
            first_data = data[0]
            #print(first_data)
            data_updated = float(first_data[1:])
            return data_updated
        except ValueError:
            str(data)

df["Revenue"].fillna(-1, inplace = True)
df["Min Revenue"] = df["Revenue"].apply(get_min_revenue)
lowest_revenue = df["Min Revenue"].min()

print(f"{lowest_revenue}$ - the lowest revenue")


# --------------------------------------------
# THE OLDEST AND THE NEWEST COMPANY FOUND YEAR
# --------------------------------------------

def get_newest_company(data):
    if data > 0:  
        return int(data)
    
df["Last founded"] = df["Founded"].apply(get_newest_company)
print(f"The newest company was found in {int(df['Last founded'].max())},\nThe oldest was found in {int(df['Last founded'].min())}")

# !!!!!!
#print(df.groupby(by = "Job Title")["Revenue"].max())
# print(revenue_job)

# ---------------------------------
# SALARY MIN AND SALARY MAX AVERAGE
# ---------------------------------

#print(df["Salary Estimate"])

df["Salary Estimate"].fillna(-1, inplace = True)
df["Salary Estimate"].replace(-1, "None")
#print(pd.isnull(df["Salary Estimate"]).head(2)) # перевірити чи є нульові значення в перших 2 рядках
def get_avg_min_salary(data):
    
        data = data.replace("(Glassdoor est.)", '')
        remove_k = data.replace("K", "")
        #print(remove_k)
        split_on_two_parts = remove_k.split("-")
        #print(split_on_two_parts)

        min_salary = split_on_two_parts[0]
        #max_salary = split_on_two_parts[1]

        min_salary_remove_sign = min_salary[1:]
        #print(min_salary_remove_sign)
        #max_salary_remove_sign = max_salary[1:]

        if min_salary_remove_sign == "":
            print(5)
        else:
            return float(min_salary_remove_sign)

def get_avg_max_salary(data):
    data = data.replace("(Glassdoor est.)", "")
    remove_k = data.replace("K", "")
    split_on_two_parts = remove_k.split("-")

    max_salary = split_on_two_parts[1]

    max_salary_remove_sign = max_salary[1:] # [1:]  # від другого елементу до кінця ("Hello"[1:] -> "ello")
    #print(max_salary_remove_sign)

    if max_salary_remove_sign == "":
        print(543)
    else:
        return float(max_salary_remove_sign)

df["Average Minimum Salary"] = df["Salary Estimate"].apply(get_avg_min_salary)
min_avg = round(df["Average Minimum Salary"].mean()) # round() - округлити без остачі, якщо поставити кому та вказати число (кількість значень після коми (1,2,3,4,5)) буде остача round(f, 2)

df["Average Maximum Salary"] = df["Salary Estimate"].apply(get_avg_max_salary)
max_avg = round(df["Average Maximum Salary"].mean())

print(f'Average Minimum Salary is: ${min_avg}K\nAverage Maximum Salary is ${max_avg}K')

#print("Hello"[1:])

# ---------

df["Size"].fillna(-1, inplace = False)
#print(df["Size"])
def get_minimum_employees(data):
    
    data = data.replace("employees", "")
    
    if "to" in data:
        split_on_two_parts = data.split("to")
        #print(remove_to)

        minimum_employees = split_on_two_parts[0]

        #if data != "-1":
        return int(minimum_employees)
    
    if "+" in data:
        #global nmb
        #print("number with +, skipped")
        #continue
        data.replace("+", "")  

def get_maximum_employees(data):
    if "to" in data:
        data = data.replace("employees", "")
        #print(data)
        split_on_two_parts = data.split("to")

        maximum_employees = split_on_two_parts[1]
    

        return int(maximum_employees)

    if "+" in data:
        nmb = "number with +, skipped"
        data.replace("+", "")
        #pass
        #print(nmb)
        
        #split_on_two_parts = data.split("+")
        #maximum_employees = split_on_two_parts[0]
        #print(maximum_employees)
        #return int(maximum_employees)
        

df["Minimum employees"] = df["Size"].apply(get_minimum_employees)
df["Maximum employees"] = df["Size"].apply(get_maximum_employees)
#a.fillna(-1, inplace = True)   # fillna() - заміняє пусті значення NaN на ті які вказав користувач як аргумент
avg_min_employees = round(df["Minimum employees"].mean())  # mean() - середнє число, береться з певного стовпчика
avg_max_employees = round(df["Maximum employees"].mean())

#print(round(df["Minimum employees"].mean()))
#print(df["Size"])

print(f"Minimum average number of employees: {avg_min_employees}\nMaximum average number of employees: {avg_max_employees}")


df["Rating"] =  df["Rating"].replace(-1, 0)
print(df["Rating"])


# ---------------------
# GRAPH / PLOT CREATION
# ---------------------

import matplotlib.pyplot as plt # імпорт бібліотеки

d = df["Rating"]
d.plot(kind = "hist")   # зробити графік з видом hist гістограма за допомогою метода plot() від pandas

plt.show()  # відобразити графік
