public class Rectangle
{
    private float width;
    private float length;

    public Rectangle()
    {
        this.width = 1.0f;
        this.length = 1.0f;
    }

    public Rectangle(float width, float length)
    {
        this.width = width;
        this.length = length;
    }

    //get - set width
    public float getWidth()
    {
        return this.width;
    }
    public void setWidth()
    {
        getWidth();
    }

    //get - set length
    public float getLength()
    {
        return this.length;
    }
    public void setLength()
    {
        getLength();
    }

    //toString funct
    public String toString()
    {
        return "Rectangle[width: " + this.getWidth() + ", " + "length: " + this.getLength() + "]";
    }

    public float getArea()
    {
        return this.width * this.length;
    }

    public float getPerimeter()
    {
        return 2 * (this.width + this.length);
    }
}