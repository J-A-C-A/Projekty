import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
	public class Snake {
		private Rect[] body = new Rect[1000];
		private double bodyWidth , bodyHeight;
		private int size;
		private int tail = 0;
		private int head = 0;
		private Direction direction = Direction.RIGHT;
		//tempo poruszania węża
		private double ogWaitBetweenUpdates = 0.12f;
		private double waitTimeLeft = ogWaitBetweenUpdates;
		private Rect background; 
		public Snake(int size , double startX , double startY , double bodyWidth , double bodyHeight, Rect background) 
		{
			this.size = size;
			this.bodyWidth = bodyWidth;
			this.bodyHeight = bodyHeight;
			this.background = background;
			for(int i = 0 ; i <= size ; i++)
			{
				Rect bodyPiece = new Rect(startX + i * bodyWidth , startY , bodyWidth , bodyHeight);
				body[i] = bodyPiece;
				head++;
			}
			head--;
		}

		public void changeDirection(Direction newDirection) 
		{
			if(newDirection == Direction.RIGHT && direction != Direction.LEFT) 
			{
				direction = newDirection;				
			}
			else if (newDirection == Direction.LEFT && direction != Direction.RIGHT) 
			{
				direction = newDirection;				
			}
			else if(newDirection == Direction.UP && direction != Direction.DOWN) 
			{
				direction = newDirection;				
			}
			else if(newDirection == Direction.DOWN && direction != Direction.UP) 
			{
				direction = newDirection;				
			}
		}
		public void update(double dt) 
		{
			if(waitTimeLeft > 0) 
			{
				waitTimeLeft -= dt;
				return;
			}
			// jak wąż przetnie siebie to program wraca do menu
			if(intersectingWithSelf()) 
			{
				Window.getWindow().changeState(2); 
			}
			waitTimeLeft = ogWaitBetweenUpdates;
			double newX = 0;
			double newY = 0;
			if(direction == Direction.RIGHT) 
			{
				newX = body[head].x + bodyWidth;
				newY = body[head].y;
			} 
			else if(direction == Direction.LEFT) 
			{
				newX = body[head].x - bodyWidth;
				newY = body[head].y;
			}
			else if(direction == Direction.UP) 
			{
				newX = body[head].x;
				newY = body[head].y - bodyHeight;
			}
			else if (direction == Direction.DOWN) 
			{
				newX = body[head].x;
				newY = body[head].y + bodyHeight;
			}
			body[(head + 1) % body.length] = body[tail];
			body[tail] = null;
			head = (head + 1) % body.length;
			tail = (tail + 1) % body.length;
			
			body[head].x = newX;
			body[head].y = newY;
		}
		//co gdy wąż przecina siebie 
		public  boolean intersectingWithSelf() 
		{
			Rect headR = body[head]; //R od Rectangle
			return intersectingWithRect(headR) || intersectingWithScreenBoundaries(headR); //to będzie robilo to samo
		}
		public boolean intersectingWithRect(Rect rect) 
		{
			for(int i = tail; i != head; i = (i + 1) % body.length ) 
			{
				if(intersecting(rect, body[i])) return true; //sprawwdzamy rect a nie head
			}
			return false;
		}
		public boolean intersecting(Rect r1, Rect r2) 
		{ //Mówi nam czy dwa prostokąty 1 i 2 się przecinają
			return (r1.x >= r2.x && r1.x + r1.width <= r2.x + r2.width &&
					r1.y >= r2.y && r1.y + r1.height <= r2.y + r2.height); //zwraca wartość booleanowską
		}
		public void grow() 
		{
			double newX = 0;
			double newY = 0;
			if(direction == Direction.RIGHT) 
			{
				newX = body[tail].x - bodyWidth;
				newY = body[tail].y;
			} else if(direction == Direction.LEFT) 
			{
				newX = body[tail].x + bodyWidth;
				newY = body[tail].y;
			}
			else if(direction == Direction.UP) 
			{
				newX = body[tail].x;
				newY = body[tail].y + bodyHeight;
			}
			else if (direction == Direction.DOWN) 
			{
				newX = body[tail].x;
				newY = body[tail].y - bodyHeight;
			}
			Rect newBodyPiece = new Rect(newX, newY, bodyWidth, bodyHeight);
		    tail = (tail == 0) ? body.length - 1 : tail - 1; // Poprawka tutaj
		    body[tail] = newBodyPiece;
		}
		public boolean intersectingWithScreenBoundaries(Rect head) 
		{ //skąd wiemy że dotyka granicy?
			return(head.x < background.x || (head.x + head.width) > background.x + background.width ||
				   head.y < background.y || (head.y + head.height) > background.y + background.height);
		}
		public void draw(Graphics2D g2) 
		{
			//wąż podzielony na segmenty złożone z 4 małych prostokątów
			for(int i = tail ; i != head; i = (i + 1) % body.length) 
			{
				Rect piece = body[i];
				double subWidth = (piece.width - 6.0) / 2.0;
				double subHeight = (piece.height - 6.0) / 2.0;
				g2.setColor(Color.GREEN);
				g2.fill(new Rectangle2D.Double(piece.x + 2.0 , piece.y + 2.0 , subWidth , subHeight));
				g2.fill(new Rectangle2D.Double(piece.x + 4.0 + subWidth , piece.y + 2.0 , subWidth , subHeight));
				g2.fill(new Rectangle2D.Double(piece.x + 2.0 , piece.y + 4.0 + subHeight , subWidth , subHeight));
				g2.fill(new Rectangle2D.Double(piece.x + 4.0 + subWidth , piece.y + 4.0 + subHeight , subWidth , subHeight));
 			}
		}
	}