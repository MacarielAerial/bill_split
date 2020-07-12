import data
from bill_split import Split

obj = Split(data.PPL_DISH, data.DISH_P)
obj.display_final()
obj.display_individual()
