"replace paragraph"

a = """he first challenge is the internet connection and availability. Due to demonetization,
    many people would go cashless. Therefore, they would resort to E-cash and E-payment. However, in many developing nations,
    internet connectivity is quite poor. Hence, this forms a major challenge for any government which intends to implement demonetization
    Cash shortage is a natural consequence of demonetization. "
    The scarcity of cash can certainly lead to chaos. This is exactly what took place during the 2010"""
r = a.replace("is","are")
print(r)

m  = a.count("and")

n = a.count("are")

print(m)
print(n)