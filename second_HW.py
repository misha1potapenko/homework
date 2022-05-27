wheather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
'была', '+5', 'градусов']
for_change_list = (1, 3, 5, 7, 12, 14)
for i in for_change_list:
    wheather.insert(i, '"')
print(wheather)
wheather[2] = '05'
wheather[13] = '+05'
new_wheather = ' '.join(wheather)
print(new_wheather)