import matplotlib.pyplot as plt
import sqlite3

# First connect to database/SQLite, and get the value
SQL = sqlite3.connect('climate.db')
curv = SQL.cursor()
curv.execute("SELECT * FROM ClimateData")
allRows = curv.fetchall()
SQL.close()

# append the list with the data
years = [eachRow[0] for eachRow in allRows]
co2 = [eachRow[1] for eachRow in allRows]
temp = [eachRow[2] for eachRow in allRows]

# Plotting the data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")