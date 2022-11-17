menu = [[1,4],[2,4.5],[3,5.0],[4,2.0],[5,1.5]]
a,b = input().split()
a,b = int(a),int(b)
print(f"Total: R$ {menu[a-1][1]*b:.2f}")
