import matplotlib.pyplot as ploter

x = [i for i in range(10)]
y = [i for i in range(10, 0, -1)]

employee = ["Thomas Harrison\n", "\nDominiga Antonio", "Alice Fisher\n", "\nRosemary Burnwood"]
sale = [53000, 18290, 73600, 45280]

ploter.bar(employee, sale, width=0.5)
ploter.xlabel("Sales Representation")
ploter.ylabel("Transaction amount")
ploter.title("Annual results")
ploter.show()