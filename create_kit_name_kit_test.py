import sender_stand_request
import data

def get_kit_body(name):
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def get_new_user_token():
    user_body = data.user_body
    response = sender_stand_request.post_create_new_user(user_body)
    return response.json()["authToken"]

def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

def test1_create_kit_1_letter_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test_1_kit_name)
    positive_assert(current_kit_body)

def test2_create_kit_511_letters_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test_2_kit_name)
    positive_assert(current_kit_body)

def test3_create_kit_without_name():
    current_kit_body = get_kit_body(data.test_3_kit_name)
    negative_assert_400(current_kit_body)

def test4_create_kit_512_letters_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test_4_kit_name)
    negative_assert_400(current_kit_body)

def test5_create_kit_whit_special_characters_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test_5_kit_name)
    positive_assert(current_kit_body)

def test6_create_kit_whit_spaces_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test_6_kit_name)
    positive_assert(current_kit_body)

def test7_create_kit_whit_numbers_in_the_name_success_response():
    current_kit_body = get_kit_body(data.test_7_kit_name)
    positive_assert(current_kit_body)

def test8_create_kit_without_name_parameter():
    current_kit_body = data.kit_body.copy()
    current_kit_body.pop("name")
    negative_assert_400(current_kit_body)

def test9_create_kit_a_different_type_of_parameter_in_the_name():
    current_kit_body = get_kit_body(data.test_7_kit_name)
    negative_assert_400(current_kit_body)