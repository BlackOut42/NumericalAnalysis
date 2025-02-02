
def newton_raphson(f, p0, TOL=1e-6, N=50):
    print("{:<10} {:<15} {:<15} ".format("Iteration", "po", "p1"))
    df = derivative_approx(f,p0)
    for i in range(N):
        if df == 0:
            print( "Derivative is zero at p0, method cannot continue.")
            return

        p = p0 - f(p0) / df

        if abs(p - p0) < TOL:
            return p  # Procedure completed successfully
        print("{:<10} {:<15.9f} {:<15.9f} ".format(i, p0, p))
        p0 = p
    return p


def derivative_approx(f, x, h=1e-6):
    return (f(x + h) - f(x)) / h