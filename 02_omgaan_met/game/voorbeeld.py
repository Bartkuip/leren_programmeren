def BerekenBtw(excl_btw, btw) -> float:
    incl_btw = excl_btw * btw
    excl_btw += incl_btw
    return excl_btw

print(excl_btw)