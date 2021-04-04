url = "http://naver.com"
my_str = url.replace("http://","") 

my_str = my_str[0:5]

password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("생성된 비밀번호 : " + password)
