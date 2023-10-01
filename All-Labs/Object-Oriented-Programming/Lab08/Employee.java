public class Employee extends Person
{
    private String ID;
    private double salary;

    public Employee()
    {
        super();
        this.ID = "";
        this.salary = 0.0;
    }

    public Employee(String ID, double salary, String name, int birthYear)
    {
        super(name, birthYear);
        this.ID = ID;
        this.salary = salary;
    }

    public String getID()
    {
        return this.ID;
    }

    public void setID(String ID)
    {
        this.ID = ID;
    }

    public double getSalary()
    {
        return this.salary;
    }

    public void setSalary(double salary)
    {
        this.salary = salary;
    }

    public String toString()
    {
        return "Employee[name = " + getName() + ", birth year = " + getBirthYear() + ", ID = " + this.ID + ", salary = " + this.salary + "]";
    }
}