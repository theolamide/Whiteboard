def alphabetical_order(arr):

    sorted_list = sorted(arr)
    for i in range(0, len(sorted_list)):
        print(sorted_list[i])


alphabetical_order(['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot',
                    'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive'])
