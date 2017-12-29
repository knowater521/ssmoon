import dis


def test():
    b=100
    def acfun():
        print(b)



# print(test.__code__.co_cellvars)

dis.dis(test)


# vm = VirtualMachine()
# vm.run_code(test.__code__)
# print(test.__code__.co_cellvars)
# print(test.__code__.co_consts[2].co_freevars)