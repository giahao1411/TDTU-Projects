public abstract class StudentB3
{
    protected String name;
    protected double gpa;

    public StudentB3()
    {
        this("", 0.0);
    }

    public StudentB3(String name, double gpa)
    {
        this.name = name;
        this.gpa = gpa;
    }

    public String getName()
    {
        return this.name;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public double getGPA()
    {
        return this.gpa;
    }

    public void setGPA(double gpa)
    {
        this.gpa = gpa;
    }

    public abstract String getRank();
}