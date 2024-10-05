import kiteapp as kt
from time import sleep
with open('enctoken.txt', 'r') as rd:
	token = rd.read()
kite = kt.KiteApp("Naitik", "VTE578", token)
kws = kite.kws() 



# Place Order
oid = kite.place_order(variety="amo", exchange='NSE',
		tradingsymbol='SBIN', transaction_type='BUY',
		quantity=5, product='MIS', order_type="LIMIT",
		price=820, validity="DAY")


print(oid)
'''
order = kite.orders()

print(order)

holding = kite.holdings()

print(holding)
'''