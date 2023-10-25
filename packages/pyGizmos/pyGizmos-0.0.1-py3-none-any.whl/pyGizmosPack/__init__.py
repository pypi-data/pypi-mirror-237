import time
import sys

activeTypeWait = 0.2



def type(string = "", delay = 0.06):
  for char in string:
    time.sleep(delay)
    sys.stdout.write(char)
    sys.stdout.flush()

def receipt(store, item, amount = 1, currency = "$", price = 0.00):
  printed = 1
  store = store.title()
  item = item.title()

  print(store)
  print("-" * 45, "\n")
  while printed <= amount:
    print("{:<39}".format(item) + currency + format(price, ".2f"))
    printed += 1

  print("-" * 45, "\n")

type("Hello World\n\nHello")