weight = float(input("您的体重是？（kg）"))
height = float(input("您的身高是？（m）"))
BMI = float(weight/(height*height))

if BMI<18.5 :
    print("太轻啦！")
elif 18.5<=BMI<=23.9:
    print("非常健康！")
elif 24 <= BMI <= 27:
    print("有点重哦！")
elif 28 <= BMI <= 32:
    print("该减肥啦！")
else:
    print("不减肥不行啦！！！")
