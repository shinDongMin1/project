import javax.swing.*;
import java.awt.*;
import java.lang.*;

abstract class Figure{
	abstract void area();
	abstract void girth();
	abstract void draw();
}

class Circle extends Figure{
	int r;
	
	Circle(){r=1;}
	Circle(int x){r=x;}
	public void area() {System.out.println("원의 넓이="+r*r*3.14);}
	public void girth() {System.out.println("원의 둘레="+r*2*3.14);}
	public void draw() {
		class User extends JComponent{
			public void paintComponent(Graphics g) {
				g.drawOval(20, 20, r+20, r+20);
			}
		}
		JFrame frame = new JFrame();
		final int FRAME_WIDTH = 400;
		final int FRAME_HEIGHT = 400;
		frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);
		frame.setTitle("원 그리기");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		User component = new User();
		frame.add(component);
		frame.setVisible(true);
		/*double x; double y; 
		for(x=-2*r;x <= 2*r; x+=2) {
			for(y=-r;y<=r;y++) {
				if((x*x+y*y)>=r*r-r/1.3 &&(x*x+y*y)<=r*r+r/1.3)
					System.out.print("*");
				else
					System.out.print(" ");
			}
			System.out.println("");*/
	}
}

	
class Square extends Figure{
	int line1;
	int line2;
	
	Square(){line1=1;line2=1;}
	Square(int x, int y) {line1=x;line2=y;}
	public void area() {System.out.println("사각형의 넓이="+line1*line2);}
	public void girth() {System.out.println("사각형의 둘레="+(line1*2+line2*2));}
	public void draw() {
		class User extends JComponent{
			public void paintComponent(Graphics g) {
				g.drawRect(20, 20, line1+20, line2+20);
			}
		}
		JFrame frame = new JFrame();
		final int FRAME_WIDTH = 400;
		final int FRAME_HEIGHT = 400;
		frame.setSize(FRAME_WIDTH, FRAME_HEIGHT);
		frame.setTitle("사각형 그리기");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		User component = new User();
		frame.add(component);
		frame.setVisible(true);
		/*
		for(int i = 0; i < line1; i++) {
			for(int j=0; j < line2; j++) {
		        System.out.print("*");
			}
	    System.out.println("");
		}*/
	}

}
public class Test3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub		
		Circle c = new Circle(100);
		c.area();
		c.girth();
		c.draw();
		Square s = new Square(100,100);
		s.area();
		s.girth();
		s.draw();

	}

}
