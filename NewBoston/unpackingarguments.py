def health_cal(age,apples,cigs):
    answer = (100 - age) + (apples * 3.5) - (cigs * 2)
    print(answer)


harsh = [22,4,3]
health_cal(harsh[0],harsh[1],harsh[2])
health_cal(*harsh)#pass all paras,unpacks arguments
