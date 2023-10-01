class ImageLoader
{
    private static ImageLoader imageLoader = null;

    private ImageLoader()
    {
    }

    public static ImageLoader getInstance()
    {
        if (imageLoader == null)
        {
            imageLoader = new ImageLoader();
        }
        return imageLoader;
    }

    public String loadImage()
    {
        return "Loaded successfully";
    }
}

//Main class
public class Ex2
{
    public static void main(String[] args)
    {
        ImageLoader imgLoader = ImageLoader.getInstance();
        System.out.println(imgLoader.loadImage());
    }
}