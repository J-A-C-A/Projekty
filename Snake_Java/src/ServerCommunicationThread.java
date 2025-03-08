import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class ServerCommunicationThread extends Thread
{
	private Socket clientSocket;
	public ServerCommunicationThread(Socket clientSocket) 
	{
		this.clientSocket = clientSocket;
	}
	@Override 
	public void run() 
	{
		try 
		{
			BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
			PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
			System.out.println("SERVER: IN and OUT streams opened. Starting receiving data...");
			out.println("Welcome to the server. I'm waiting for the data.");
			out.flush();
			String inputLine;
			while ((inputLine = in.readLine()) != null) 
			{
				if (inputLine.equals("end")) 
				{
					System.exit(0);;
				}
				if (inputLine.equals("time")) 
				{
					double time = Time.getTime();
					out.println(Math.round(time));
				}
				out.flush();
			}
			System.out.println("SERVER: Ending sequence received. Closing streams and sockets.");
			out.close();
			in.close();
			clientSocket.close();
		} 
		catch (IOException e) 
		{
			e.printStackTrace();
			System.exit(1);
		}
	}	
}