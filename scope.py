# '''
# LEGB
# Local, Enclosing, Gobal, Built-in
# '''
# import builtins
#
# print(dir(builtins))
#
# def my_min():
#     pass
#
# m = min([5,1,4,2,3])
# print(m)
#
# #x = "global x"
#
# def test(z):
#     x = "local x"
#     #print(y)
#     print(z)
#
#
# test("local z")
# #print(z)

x = "global x"

def outer():
    x = "outer x"

    def inner():
        #x = "inner x"
        print(x)

    inner()
    print(x)

outer()
print(x)

#End
