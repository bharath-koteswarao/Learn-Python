if __name__ == '__main__':
    """
    List of all available functions
    
    conjugate()     Gives the conjugate part
    
    abs()       Gives the mod value of a complex number
    
    real()      Gives the real part of a complex number
    
    imag()      Gives the imaginary part of a complex number
    """
    a = complex(1, 2)
    print(a.__abs__())
    print(a.conjugate())
    print(a.real)
    print(a.imag)
    pass
