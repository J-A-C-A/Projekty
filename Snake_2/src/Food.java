import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;

public class Food {
	private Rect background;
	private Snake snake;
	private int width, height;
	private Color color;
	private Rect rect; 
	protected static int applesEaten;
	private int xPadding; //jak bardzo wycentrować w kratce
	protected boolean isSpawned = false; //na początku jedzenia nie ma dlatego false
	
	public Food(Rect background, Snake snake, int width, int height, Color color){ //potrzebujemy jakiś referencji do tła oraz do węża z klasy Snake
		this.background = background; //inicjalizujemy wszystkie zmienne
		this.snake = snake;
		this.width = width;
		this.height = height;
		this.color = color.RED;
		this.rect = new Rect(0, 0, width, height); //potrzebujemy nowego Rectangle ktory bedzie reprezentował jedzenie Food
		xPadding = (int)((Constants.TILE_WIDTH - this.width)/2.0); //to nam da jak dużo marginesu potrzebujemy aby ustawić to w dobrej pozycji
	}
	
	public void spawn() { //musimy znalezc takie miejsce na tle, gdzie obecnie nie ma żadnego jedzenia, musimy użyć funkcji do losowania
		do { //będzie szukać losowej pozycji, jeśli akurat ta będzie zajęta to szuka innej, tak dlugo aż nie znajdzie
			//generujemy losową liczbę, mnożymy ją przez iloraz szerokości i szerokości jednej kratki co daje nam liczbę pomiędzy 0 a liczbą kolumn jaka jest czyli np, 1,2,3,4 i mnożymy to razy szerokość kratki aby zkonwertować to do realnej pozycji x i dodajemy pozycję x
			double randX = (int)(Math.random() * (int)(background.width / Constants.TILE_WIDTH))* Constants.TILE_WIDTH + background.x;
			double randY = (int)(Math.random() * (int)(background.height / Constants.TILE_WIDTH))* Constants.TILE_WIDTH + background.y; //mnożymy razy tile width bo to są kratki kwadratowe
			this.rect.x = randX;
			this.rect.y = randY;
		}while(snake.intersectingWithRect(this.rect));
		this.isSpawned = true; //jedzenie jest zespawnowane
	}
	//całe spawn powinno nam zwrócić takie liczby x i y że nie przecinają się z wężem ani z jedzeniem
	
	public void update(double dt) {
		if(snake.intersectingWithRect(this.rect)) {
			snake.grow(); //funkcja na rośnięcie węża
			this.rect.x = -100;
			this.rect.y = -100;
			isSpawned = false;
			applesEaten += 1;
		}
	}
	public void draw(Graphics2D g2) {
		g2.setColor(color.RED);
		g2.fillRect((int)this.rect.x + xPadding, (int)this.rect.y + xPadding, width, height); //this.rect.y+ xPadding bo tile to jest kwadrat, a rect trzyma wszystkie informacje o width i height
	
	}
}
