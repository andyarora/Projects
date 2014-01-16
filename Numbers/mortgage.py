

def monthly_mortgage(r, n, p):
	"r - interest, n - duration, p - principal"
	r = (r/12)/100
	return (p * r * ((1+r) ** n))/(((1+r)**n) - 1)

print '{0:.2f}'.format(monthly_mortgage(float(raw_input("r: ")), \
	float(raw_input("n: ")), float(raw_input("p: "))))
