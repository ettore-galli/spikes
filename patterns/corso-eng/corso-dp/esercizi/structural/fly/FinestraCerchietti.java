package fly;
import java.awt.*;
import java.util.HashMap;
import java.awt.Color;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

public class FinestraCerchietti extends JFrame{
   private static final Color colors[] = { Color.red, Color.blue,
                                           Color.yellow, Color.orange,
                                           Color.black,  Color.white };
   private static final int WIDTH = 400,
                            HEIGHT = 400,
                            NUMBER_OF_CIRCLES = 1000;

   public FinestraCerchietti() {
      Container contentPane = getContentPane();
      
      JButton button = new JButton("Draw Circle");
      final JPanel  panel  = new JPanel();

      contentPane.add(panel,  BorderLayout.CENTER);
      contentPane.add(button, BorderLayout.SOUTH);
      setSize(WIDTH,HEIGHT);
      setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      setVisible(true);

      button.addActionListener(new ActionListener() {
         public void actionPerformed(ActionEvent event) {
            Graphics g = panel.getGraphics();
            for(int i=0; i < NUMBER_OF_CIRCLES; ++i) {
                Circle circle = CircleFactory.getCircle(getRandomColor());
                circle.draw(g, getRandomX(), getRandomY(),getRandomR());
               //Since we have 6 different colors, we have 6 objects created.
            }
          }
      });
   }
  
   private int getRandomX() {
      return (int)(Math.random()*WIDTH );
   }
   private int getRandomY() {
      return (int)(Math.random()*HEIGHT);
   }
   private int getRandomR() {
      return (int)(Math.random()*(HEIGHT/10));
   }
   private Color getRandomColor() {
      return colors[(int)(Math.random()*colors.length)];
   }
}





