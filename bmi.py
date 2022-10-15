weight = input('請輸入體重:')
height = input('請輸入身高:')
weight = int(weight)
height = int(height)
height = height / 100
bmi = weight / height / height 
bmi = int(bmi)
if bmi < 18.5:
    print('體重過輕')
elif bmi >= 18.5 or bmi <= 24:
    print('體重正常' ,'bmi' ,bmi)
elif bmi >24:
    print('體重過重')
