import action


def menu_choice(user_choice):
    if user_choice == '1':
        action.new_pers()
    elif user_choice == '2':
        action.find_someone()
    elif user_choice =='3':
        action.get_list_phones()