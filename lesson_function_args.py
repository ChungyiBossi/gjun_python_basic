import pprint
def _save_database(info_dictionary):
    print("Save to DB complete!")
    pprint.pprint(info_dictionary)

# 會員系統的流程
def handle_membership_creation(name, id, phone, *hobbies, **other_infomation):
    gender = other_infomation['gender'] if 'gender' in other_infomation else "Unknown"
    age = other_infomation['age'] if 'age' in other_infomation else "Unknown"
    member_infomation = {
        'member_name': name,
        'member_personal_id': id,
        'member_cellphone_number': phone,
        'member_hobby': hobbies,
        'member_gender': gender,
        'member_age': age
    }

    _save_database(info_dictionary=member_infomation)

if __name__ == '__main__':
    hobby = ['coding', 'biking', 'video game']
    info = {
        'gender': 'male',
        # 'age': 30,
        'born_city': 'Taichung' 
    }
    # handle_membership_creation("Chung Yi", 'B1263545645', '0912345678', *hobby, **info)
    handle_membership_creation(
        "Chung Yi", 'B1263545645', '0912345678', 
        'coding', 'biking', 'video game', 'basketball', 
        age=30, born_city='Taichung'
    )