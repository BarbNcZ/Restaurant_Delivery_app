import os

restaurants = [{'Name':'Bambino', 'Category':'Italian', 'Active':False},
                {'Name':'Pizza Hut', 'Category':'Italian', 'Active':True},
                {'Name':'Jun Sushi', 'Category':'Japanese', 'Active':True}]

def showing_app_name():
    print('\nＴｈｅ Ｈｕｎｇｒｙ Ａｐｐ！\n')

def showing_subtitle(text):
    os.system('cls')
    line = '-' * len(text)
    print(line)
    print(text)
    print(line)
    print()

def return_the_main_menu():
    input('\nPress any key to go back to options list. ')
    main()

def invalid_option():
    print('Invalid option!')
    return_the_main_menu()

def exiting_app():
    showing_subtitle('Exiting...')

def showing_options():
    print('1. Add Restaurants')
    print('2. List Restaurants')
    print('3. Change Restaurante Status')
    print('4. Exit\n')

def listed_restaurants():
    showing_subtitle('Listing all the restaurants')

    print(f'{'Restaurant Name'.ljust(22)} {'Category'.ljust(22)} {'Status'}\n')
    for restaurant in restaurants:
        restaurant_name = restaurant['Name']
        restaurant_category = restaurant['Category']
        restaurant_status = 'Activated' if restaurant['Active'] else 'Deactivated'
        print(f'- {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_status}')
    return_the_main_menu()

def add_new_restaurant():
    showing_subtitle('Add a new Restaurant')
    restaurant_name = input('Enter the name of the Restaurant: ')
    category = input(f'Enter the category of the restaurant {restaurant_name}: ')
    restaurant_data = {'Name':restaurant_name, 'Category':category, 'Active':False}
    restaurants.append(restaurant_data)
    print(f'\nThe restaurant {restaurant_name} has been successfully added!')
    return_the_main_menu()

def change_restaurant_status():
    showing_subtitle('Changing the restaurante status')
    restaurant_name = input('Enter the name of the restaurant whose status you want to change: ')
    restaurant_found = True

    for restaurant in restaurants:
        if restaurant_name == restaurant['Name']:
            restaurant_found = True
            restaurant['Active'] = not restaurant['Active']
            message = f'The restaurant {restaurant_name} was successfully activated' if restaurant['Active'] else f'The restaurant {restaurant_name} was successfully deactivated'
            print(message)

    if not restaurant_found:
        print('The restaurant was not found.\n')


    return_the_main_menu()

def choosing_option():
    try:    
        chosen_option = int(input('Choose an option: '))
        
        if chosen_option == 1:
            add_new_restaurant()

        elif chosen_option == 2:
            listed_restaurants()

        elif chosen_option == 3:
            change_restaurant_status()

        elif chosen_option == 4:
            exiting_app()

        else:
            invalid_option()
    except:
        invalid_option()

def main():
    os.system('cls')
    showing_app_name()
    showing_options()
    choosing_option()

if __name__ == '__main__':
    main()