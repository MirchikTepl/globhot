import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789qwertyuiopasdfghjklzxcvbnm"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def gen_zasyxa():
    zasyxa = ["Если в вашем регионе преобладал и преобладает сухой климат, то всё стабильно, но если у вас должна преобладать влага, а сейчас засуха, то ситуация критическая. Глоб.потепление уже у вас, дабы не ухудшить ситуацию читайте остальные проблемы тут /problem"]
    return zasyxa

def gen_problem():
    problem = ["Опиши проблему"]
    return problem

def gen_temp():
    temp = ["Опиши проблему"]
    return temp

def gen_elektro():
    elektro = ["Возможно перегрузка сети, из-за которой в дальнейшем может быть глоб.потепление"]
    return elektro

def gen_gryaz():
    gryaz = ["Если в вашем регионе обнаружена экологическая проблема, свящанная с загрязнением улиц, воды и т.д., то это очень плохо. Рекомендовано пожаловаться в правительство и немедленно устранить проблему, которая в дальнейшем приведёт к глоб.потеплению"]
    return gryaz


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "ОРЕЛ"
    else:
        return "РЕШКА"