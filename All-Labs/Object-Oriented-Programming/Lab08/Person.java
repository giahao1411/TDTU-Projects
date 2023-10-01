public class Person 
{
    protected String name;
    protected int birthYear;

    public Person()
    {
        this("", 2023);
    }

    public Person(String name, int birthYear)
    {
        this.name = name;
        this.birthYear = birthYear;
    }

    public String getName()
    {
        return this.name;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public int getBirthYear()
    {
        return this.birthYear;
    }

    public void setBirthYear(int birthYear)
    {
        this.birthYear = birthYear;
    }

    public String toString()
    {
        return "Person[name = " + this.name + ", birth year = " + this.birthYear + "]";
    }
}
