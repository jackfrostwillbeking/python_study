print('金額を入力してください 単位:¥')
budget = int(input())
product_val = 0
inventory = []

def calc_change(change):
    money_unit = (10000,5000,1000,500,100,50,10,5,1)
    for I in money_unit:
        q,mod = divmod(change,I)
        change = mod
        print(str(I)+'円: '+str(q)+'枚')

while budget != 0:
    print('いくらの商品を購入しますか？ 単位:¥')
    product_val = int(input())
    if product_val > budget:
        print('投入額を超えています。入力し直してください。')
        product_val = 0
    else:
        print('¥ '+str(product_val)+'の商品を購入しました。')
        inventory.append(product_val)
        budget = budget - product_val
        print('残高残り:¥ '+str(budget))
    while budget != 0:
        print('続けて買い物しますか？ Yes/No')
        continue_flg = input()
        if continue_flg == 'No':
            change = budget
            budget = 0
        if continue_flg == 'Yes':
            break

print('購入商品')
print(*inventory)
print('お釣り:'+str(change)+'円')
calc_change(change)