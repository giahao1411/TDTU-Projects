public class Student
{
    private int id;
    private String firstName;
    private String lastName;

    public Student(int id, String firstName, String lastName)
    {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    //get - set id
    public int getID()
    {
        return this.id;
    }
    public void setID()
    {
        getID();
    }

    //get - set first name
    public String getFirstName()
    {
        return this.firstName;
    }
    public void setFirstName()
    {
        getFirstName();
    }

    //get - set last name
    public String getLastName()
    {
        return this.lastName;
    }
    public void setLastName()
    {
        getLastName();
    }

    public String getName()
    {
        return getFirstName() + " " + getLastName();
    }

    public String toString()
    {
        return "Student[id = " + this.getID() + ", firstName = " + this.getFirstName() + ", lastName = " + this.getLastName() + "]";
    }
}