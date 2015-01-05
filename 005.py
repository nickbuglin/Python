from urllib import request

# Retrieve the webpage as a string
response = request.urlopen("http://ichart.finance.yahoo.com/table.csv?s=JPM&d=1&e=5&f=2015&g=d&a=1&b=5&c=-1635&ignore=.csv")
csv = response.read()

# Save the string to a file
csvstr = str(csv).strip("b'")

lines = csvstr.split("\\n")
f = open("historical.csv", "w")
for line in lines:
   f.write(line + "\n")
f.close()