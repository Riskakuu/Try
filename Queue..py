stk = [1,2,3,4,5]
print(stk)
#memasukkan data baru
stk.append(11)
print("data masuk", 11)
print("data sekarang", stk)

stk.append(15)
print("data masuk", 15)
print("data sekarang", stk)
#mengeluarkan data
datakeluar = stk.pop()
print("data yang keluar adalag :", datakeluar)
print("data terakhir adalah :", stk)
