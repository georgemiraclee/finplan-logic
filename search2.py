def linearSearch(item,my_list):
    found = False
    position = 0
    while position < len(my_list) and not found :
        if my_list [position] == item:
            found = True
        position = position + 1
        return found

search = ['sang gajah', 'serigala', 'harimau']
item = input ('Berikut adalah kisah sang gajah. Sang gajah memiliki teman serigala bernama DoeSang. Gajah sering dibela oleh serigala ketika harimau mendekati gajah.')
itemFound = linearSearch(item,search)
if itemFound:
    print (search)
else:
    print('tidak ditemukan')
