public class House
{
    private String houseCode;
    private int numOfBedRoom;
    private boolean hasSwimmingPool;
    private double area;
    private double costPerSquareMeter;

    public House()
    {
        this.houseCode = "A01";
        this.numOfBedRoom = 2;
        this.hasSwimmingPool = false;
        this.area = 0.0;
        this.costPerSquareMeter = 0.0;
    }

    public House(String houseCode, int numOfBedRoom, boolean hasSwimmingPool, double area, double costPerSquareMeter)
    {
        this.houseCode = houseCode;
        this.numOfBedRoom = numOfBedRoom;
        this.hasSwimmingPool = hasSwimmingPool;
        this.area = area;
        this.costPerSquareMeter = costPerSquareMeter;
    }

    //get - set house code
    public String getHouseCode()
    {
        return this.houseCode;
    }
    public void setHouseCode()
    {
        getHouseCode();
    }

    //get - set number of bed room
    public int getNumOfBedRoom()
    {
        return this.numOfBedRoom;
    }
    public void setNumOfBedRoom()
    {
        getNumOfBedRoom();
    }

    //set - get has swimming pool
    public boolean getHasSwimmingPool()
    {
        return this.hasSwimmingPool;
    }
    public void setHasSwimmingPool()
    {
        getHasSwimmingPool();
    }

    //set - get area
    public double getArea()
    {
        return this.area;
    }
    public void setArea()
    {
        getArea();
    }

    //set - get cost per square meter
    public double getCostPerSquareMeter()
    {
        return this.costPerSquareMeter;
    }
    public void setCostPerSquareMeter()
    {
        getCostPerSquareMeter();
    }

    public double calculateSellingPrice()
    {
        double SubTotal = area * costPerSquareMeter;

        if(hasSwimmingPool)
            SubTotal *= 1.5;
        return SubTotal;
    }

    public String toString()
    {
        return "House[" + houseCode + ", " + numOfBedRoom + ", " + hasSwimmingPool + ", " + calculateSellingPrice() + "]";
    }
}