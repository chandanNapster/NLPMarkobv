from Product import products as products
from Product import product as product

class main():

    def getData():
        p1 = product("Refrigerator A", 999.90, 0.751)
        p2 = product("Cell phone", 2199.12, 0.00000899)
        p3 = product("TV 55`", 4346.99, 0.400)
        p4 = product("TV 50`", 3999.90, 0.290)
        p5 = product("TV 42`", 2999.9, 0.200)
        p6 = product("Notebook A", 2499.90, 0.0035)
        p7 = product("Ventilator", 199.90, 0.496)
        p8 = product("Microwave A", 308.66, 0.0424)
        p9 = product("Microwave B", 429.90, 0.0544)
        p10 = product("Microwave C", 299.29, 0.0319)
        p11 = product("Refrigerator B", 849.0, 0.635)
        p12 = product("Refrigerator C", 1199.89, 0.870)
        p13 = product("Notebook B", 1999.90, 0.498)
        p14 = product("Notebook C", 3999.0, 0.527)

        prods = products()
        prods.setProdList(p1)
        prods.setProdList(p2)
        prods.setProdList(p3)
        prods.setProdList(p4)
        prods.setProdList(p5)
        prods.setProdList(p6)
        prods.setProdList(p7)
        prods.setProdList(p8)
        prods.setProdList(p9) 
        prods.setProdList(p10)
        prods.setProdList(p11)
        prods.setProdList(p12)
        prods.setProdList(p13)
        prods.setProdList(p14)

        return prods.getProdList()