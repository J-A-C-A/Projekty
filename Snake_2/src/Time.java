/* prosta klasa która będzie mierzyła czas gry*/
public class Time 
{
	private static double timeStarted = System.nanoTime();
	//linijka poniżej będzie liczyła czas od rozpoczęcia rogdrywki do jej zakończenia, czas będzie podawany w sekundach i chyba dlatego jest 1E -9 jako chyba gotowa formułka
	public  static double getTime() 
	{
	double timeEnded = (System.nanoTime() - timeStarted) * 1E-9;
		return timeEnded;
	}
}