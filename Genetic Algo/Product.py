class products:
    
    def __init__(self):
        self.__product_list = []

    def getProdList(self):
        return self.__product_list

    def setProdList(self, p):    
        self.__product_list.append(p)

class product:
    ITEM_ID = 0
    
    def __init__(self, name, price, size):
        product.ITEM_ID = product.ITEM_ID + 1
        name = str(name).lower()
        name = name[0].upper() + name[1:]
        self.__name = name
        self.__price = price
        self.__size = size
        self.__prod_id = product.ITEM_ID

    def __str__(self):
        return "[ ITEM_ID = {0} | name = {1} | price = {2} $ | size = {3} Cubic Meter ]".format(self.__prod_id, self.__name, self.__price, self.__size) 
    
    def getProdName(self):
        return self.__name

    def getProdPrice(self):
        return self.__price

    def getProdSize(self):
        return self.__size       

    def getProdID(self):
        return self.__prod_id     

    
   

        