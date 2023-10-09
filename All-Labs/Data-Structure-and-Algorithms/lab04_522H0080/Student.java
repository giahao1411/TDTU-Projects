class Student {
    private String name;
    private double mathematics, programming, DSA1;

    public Student(String name, double mathematics, double programming, double dSA1) {
        this.name = name;
        this.mathematics = mathematics;
        this.programming = programming;
        this.DSA1 = dSA1;
    }

    public String getName() {
        return name;
    }

    public double getMathematics() {
        return mathematics;
    }

    public double getProgramming() {
        return programming;
    }

    public double getDSA1() {
        return DSA1;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setMathematics(double mathematics) {
        this.mathematics = mathematics;
    }

    public void setProgramming(double programming) {
        this.programming = programming;
    }

    public void setDSA1(double dSA1) {
        DSA1 = dSA1;
    }

    public double avgGrade() {
        return 1.0 / 3.0 * (mathematics + programming + DSA1);
    }

    @Override
    public String toString() {
        return String.format("%s - %.2f", name, avgGrade());
    }
}
