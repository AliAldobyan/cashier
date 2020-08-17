def main():

	list = []

	

	while True:
		user_input = input("Item (enter \"done\" when finished): ")
		if user_input == "done":
			break

		price = float(input("Price: "))
		quantity = int(input("Quantity: "))
		list.append({"item":user_input, "price":price, "quantity":quantity})


	print("\n---------------------\nreceipt\n---------------------\n")
	total = float(0)

	for i in list:
		print("%d %s %.3f SAR" % (i.get('quantity'), i.get('item'), i.get('quantity') * i.get('price')))
		total = total + i.get("price") * i.get("quantity")

	print("---------------------")
	print("Total Price: %.3f SAR" % (total))


if __name__ == '__main__':
	main()