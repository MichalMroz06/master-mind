def field_validation(field_id: int, user_choice: int, main_array: list[int]) -> bool:
    if user_choice < len(main_array) and user_choice >= 0:
        if main_array[field_id] == user_choice:
            return True
        else:
            return False
    else:
        return False

def is_in_array(user_choice: int, main_array: list[int]) -> bool:
    if user_choice < len(main_array) and user_choice >= 0:
        for item in main_array:
            if item == user_choice:
                return True

    return False
