def mod_add(x,y,mod):
    return (x%mod+y%mod)%mod

def mod_sub(x,y,mod):
    return (x-y)%mod

def mod_exp(x,y,mod):
    return pow(x,y,mod)

def extended_gcd(aa, bb):
        lastremainder,remainder = abs(aa), abs(bb)
        x, lastx, y, lasty = 0, 1, 1, 0
        while remainder:
            lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
            x, lastx = lastx - quotient*x, x
            y, lasty = lasty - quotient*y, y
        return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
def mod_inverse(x,mod):
    g, xx, y = extended_gcd(x, mod)
    if g!=1:
            raise ValueError
    return xx % mod

def mod_mul(x,y,mod):
    return (x*y)%mod
