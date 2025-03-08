import java.awt.event.KeyAdapter;
import java.awt.event.KeyListener;
import java.awt.event.KeyEvent;

//interpretuje ona czy guzik jest wciśnięty czy nie
public class KL extends KeyAdapter implements KeyListener{
	private boolean[]keyPressed = new boolean[1000];
	
	@Override
	public void keyPressed(KeyEvent keyEvent) {
		keyPressed[keyEvent.getKeyCode()] = true;
	}
	@Override
	public void keyReleased(KeyEvent keyEvent) {
		keyPressed[keyEvent.getKeyCode()] = false;
	}
	public boolean isKeyPressed(int keyCode) {
		return keyPressed[keyCode];
	}
}
