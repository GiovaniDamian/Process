def Com_FaleMais (p, m, v, tsfm):

    fmt = 0
    dm = 0
    if p == 1 and m > 30:
        dm = (m - 30)
        fmt = ((dm * 1.1) * v)
    if p == 2 and m > 60:
        dm = (m - 60)
        fmt = ((dm * 1.1) * v)
    if p == 3 and m > 120:
        dm = (m - 120)
        fmt = ((dm * 1.1) * v)
    return(fmt)