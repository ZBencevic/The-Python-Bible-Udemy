# get user email address
user_email = input("What is your email address? ").strip()
# slice out username
username = user_email[:user_email.index("@")]
# slice out domain name
domain_name = user_email[user_email.index("@") + 1:]
# format output message
output = f"Your username is {username} and domain name is {domain_name}"
# print output message
print(output)
