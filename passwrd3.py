import random
import string

member_table = {
"sami@email.com": {"password_hint": "What is your mother's maiden name?", "answer": "maya", "password":"qwerty123"},
"saina@email.com": {"password_hint": "What is your pet's name?", "answer": "char", "password":"password123"},
"kaalu@email.com": {"password_hint": "What is your favorite color?", "answer": "Blue", "password":"letmein"},
"akriti@email.com": {"password_hint": "What is your favorite movie?", "answer": "The Shawshank Redemption", "password":"mysecretpassword"},
"samridhi@email.com": {"password_hint": "What is your favorite book?", "answer": "The Lord of the Rings", "password":"adminpassword"}
}

def generate_temp_password(email):
 temp_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
 member_table[email]["password"] = temp_password
 return temp_password
