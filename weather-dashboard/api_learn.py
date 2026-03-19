import json
from urllib.request import urlopen

with urlopen("https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_T8W8SE0LDghETfsYH9y57N78be7nfroJeG9sQFnc") as response:
    source = response.read()
    

datas = json.loads(source)



def curr_to_usd():
  for key in datas["data"].keys():
    print(key)

  curr = input("Enter the currency: ").strip()
  amount = float(input("Enter the amount: ").strip())

  print (f"{amount} {curr} = {(datas["data"][curr])/amount} USD")


def usd_to_curr():
  for key in datas["data"].keys():
    print(key)
  curr = input("Enter the currency: ").strip()
  amount = float(input("Enter the amount: ").strip())

  print (f"{amount}USD = {((datas["data"][curr])*amount)} {curr}")


# print(json.dumps(data, indent=2))
# print(data)

print("-----WELCOME TO CURRENCY CONVERSION TOOL-----")
print("Select what you want to do:")


choice = int(input(f"1.USD to other currency.\n2.Other currency to USD.").strip())
if choice == 2:
  curr_to_usd()
elif choice == 1:
  usd_to_curr()
else:
  print("INVALID CHOICE")


