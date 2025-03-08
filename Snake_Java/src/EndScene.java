import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class EndScene extends Scene{
	private KL keyListener;
	private ML mouseListener; 
	private BufferedImage play , playPressed , exit , exitPressed; 
	private Rect playRect ,  exitRect; 
	private BufferedImage playCurrentImage , exitCurrentImage;
	private Food food;

	public EndScene(KL keyListener , ML mouseListener) 
	{
		this.keyListener = keyListener;
		this.mouseListener = mouseListener; 
	
		try 
		{
			// odczytuje plik graficzny i określa wielkość poszczególnych opcji
			BufferedImage spritesheet = ImageIO.read(new File("assets/menuSprite.png"));
			play = spritesheet.getSubimage(0,121,261,121);
			playPressed = spritesheet.getSubimage(264, 121, 261, 121);
			exit = spritesheet.getSubimage(0, 0, 233, 93);
			exitPressed = spritesheet.getSubimage(264, 0, 233, 93);
		}catch(Exception e) 
		{
			e.printStackTrace();
		}
		playCurrentImage = play;
		exitCurrentImage = exit;
		playRect = new Rect(310, 280, 150, 70);
		exitRect = new Rect(318, 355, 130, 55);
	}
	
	@Override
	public void update(double dt) 
	{
		// sprawdza czy kursor najechał na przycisk , jeśli tak to go podświetla 
		// gdy kursor zjedzie z przycisku przestaje go podkreślać
		if(mouseListener.getX() >= playRect.x && mouseListener.getX() <= playRect.x + playRect.width &&
				mouseListener.getY() >= playRect.y && mouseListener.getY() <= playRect.y + playRect.height)
			 {
					playCurrentImage = playPressed;
					if(mouseListener.isPressed) {
						Window.getWindow().changeState(1);
						Food.applesEaten = 0;
												}
			 } 
		else {
					playCurrentImage = play;
			 }
				
		if(mouseListener.getX() >= exitRect.x && mouseListener.getX() <= exitRect.x + exitRect.width &&
				mouseListener.getY() >= exitRect.y && mouseListener.getY() <= exitRect.y + exitRect.height)
				{
					exitCurrentImage = exitPressed;
					if(mouseListener.isPressed) 
					{
						System.exit(0);
					}
				} 
		   else {
					exitCurrentImage = exit;
				}
	}
	@Override
	public void draw(Graphics g) 
	{
		g.setColor(new Color(120,173,180));
		g.fillRect(0, 0, Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT);
		//wyświetla obraki z  przyciskiem "play" oraz "exit" i ustala ich lokalizacje w okienku 
		g.drawImage(playCurrentImage, (int)playRect.x, (int)playRect.y, (int)playRect.width, (int)playRect.height, null);
		g.drawImage(exitCurrentImage, (int)exitRect.x, (int)exitRect.y, (int)exitRect.width, (int)exitRect.height, null);
		g.setFont(new Font("Arial" , Font.BOLD , 40));
		g.setColor(Color.BLACK);
		g.drawString("Final score: " + String.valueOf(food.applesEaten), 270, 200);
	}
}