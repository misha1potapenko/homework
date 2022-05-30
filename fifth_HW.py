prise = [12, 24.3, 32.43, 123.02, 0.12, 0.03,
prise = [12, 24.3, 32.43, 123.02, 0.12, 0.03,
         123.4, 423.45, 23.4, 43.4, 56.6, 99]
print(id(prise))
price_rub = []
for i in prise:
    if i//1 >= 1:
        rub = i//1
        price_rub.append(int(rub))
print(price_rub)
# не смог отделить десятичные
print(f'{prise[0]} руб {int(prise[1])} руб {prise[1]} коп {prise[2]:.0f} руб {prise[3]:.0f} руб {prise[4]} коп '
      f'{prise[5]} коп {prise[6]:.0f} руб {int(prise[7])} руб {int(prise[8])} руб {int(prise[9])} руб {int(prise[10])} руб {prise[11]} руб')

prise.sort()
print(prise)
#доказательство что список тот же
print(id(prise))
prise.sort(reverse = True)

print(prise)
print(f'{prise[:5]} пять самых дорогих')
