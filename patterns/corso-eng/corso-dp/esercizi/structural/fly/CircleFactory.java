package fly;

import java.awt.Color;
import java.util.HashMap;

public class CircleFactory {
	   private static final HashMap circleByColor = new HashMap();

	   public static Circle getCircle(Color color) {
	      Circle circle = (Circle)circleByColor.get(color);

	      if(circle == null) {
	         circle = new Circle(color);
	         circleByColor.put(color, circle);
	         System.out.println("Creating " + color + " circle");
	      }
	      return circle;
	   }
}