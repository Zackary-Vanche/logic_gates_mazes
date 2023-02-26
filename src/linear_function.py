def linear_function(xa, ya, xb, yb):
    assert xa != xb
    pente = (yb - ya)/(xb - xa)
    coeff = ya - pente*xa
    return (pente, coeff)