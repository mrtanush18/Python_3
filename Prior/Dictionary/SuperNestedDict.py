# Access innermost value (main)

users_data={1: {"general": {"age": 45,"name": "John"},"car_data": {"general": {"type": "mercedes","model": "GLE"}},"additional": {"first_commit": {"list_of_attempts": [{"type": "main"}]}}}}

# 1 line code : 
# print(users_data[1]["additional"]["first_commit"]["list_of_attempts"][0]["type"])
# o/p : main

for key,value in users_data.items():
    print(value)
    for k2,v2 in value.items():
        # print(v2)
        for k3,v3 in v2.items():
            # print(v3)
            temp = type(v3)      
            if temp == dict:
                for k4,v4 in v3.items():
                    # print(v4)
                    if type(v4) == list:
                        print(v4[0]['type'])
                    
# o/p : main