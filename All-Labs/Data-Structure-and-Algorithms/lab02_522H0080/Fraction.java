class Fraction {
    private int numer = 0;
    private int denom = 1;

    public Fraction() {
    }

    public Fraction(int x, int y) {
        this.numer = x;
        this.denom = y;
    }

    public Fraction(Fraction f) {
        this.numer = f.numer;
        this.denom = f.denom;
        // this(f.numer, f.denom);
    }

    public String toString() {
        return String.format("%d/%d", numer, denom);
    }

    public boolean equals(Object obj) {
        if (obj instanceof Fraction) {
            Fraction tmp = (Fraction) obj;
            return this.numer * tmp.denom - this.denom * tmp.numer == 0;
        }
        return false;
    }
}
