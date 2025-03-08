
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import javax.swing.JFrame;

public class Window extends JFrame implements Runnable
{
	protected static Window window = null ; 
	private boolean isRunning;
	private int currentState;
	private Scene currentScene;
	
	private KL keyListener = new KL();
	private ML mouseListener = new ML();
	
	public Window(int width, int height, String title) {
		setSize(width, height); // tutaj ustalany poprzez 'set' wszystkie wartości jak wzrost czy szerokość. Dodatkowo poprzedz zmienne Resisable i visible określamy czy ma to być widoczne czy nie i dlatego przy visible mamy true ponieważ chcemy widzieć te wartości
		setTitle(title);
		setResizable(false);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		addKeyListener(keyListener);
		addMouseListener(mouseListener); 
		addMouseMotionListener(mouseListener); 
		
		isRunning = true;
		changeState(0);
	}

	public static Window getWindow() 
	{
		if(Window.window == null) 
		{
			Window.window = new Window(Constants.SCREEN_WIDTH , Constants.SCREEN_HEIGHT , Constants.SCREEN_TITLE);
		}
		return Window.window;
	}
	
	
	public void close() 
	{
		isRunning = false;
	}
	public  void changeState(int newState) 
	{
		currentState = newState;
		switch(currentState) 
		{
			case 0:
				currentScene = new MenuScene(keyListener , mouseListener);
				Time.getTime();
				break;
			case 1:
				currentScene = new GameScene(keyListener);
				break;
			case 2:
				currentScene = new EndScene(keyListener , mouseListener); 
				break;
			default:
				System.out.println("Unknown scene.");
				currentScene = null;
				break;
		}
	}
	
	public void update(double dt) 
	{
		Image dbImage = createImage(getWidth(), getHeight());
		Graphics dbg = dbImage.getGraphics();
		this.draw(dbg);
		getGraphics().drawImage(dbImage, 0, 0,this);
		currentScene.update(dt);
	}
	
	public void draw(Graphics g) 
	{ //ustawianie coloru ekranu gry.
		Graphics2D g2 = (Graphics2D)g;
		currentScene.draw(g2);
	}
	
	@Override
	public void run() 
	{ /*w metodzie 'run' będzie kod do całej głównej gry*/
		double lastFrameTime = 0.0;
		try 
		{
			while(isRunning) 
			{
				double time = Time.getTime();
				double deltaTime = time - lastFrameTime;
				lastFrameTime = time;
				update(deltaTime);
			}
		}
		catch(Exception e) 
		{
			e.printStackTrace();
		}
		this.dispose();
	}
}
