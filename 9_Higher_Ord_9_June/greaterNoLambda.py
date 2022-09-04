# Keep revising # how to print long statements in lambda fn 
# Using only lambda fn print greater no.

ans = lambda x,y: f"{x} is greater than {y}" if x>y else f"{y} is greater than {x}" if y>x else "Both equal"

print(ans(20,-40))

# o/p : 20 is greater than -40