package factoryMethodToDo;

import java.io.*;
public class Main {
	public static void main (String[] arg) throws IOException {
		// creo gli handler 		
		ConnectorHandler cTool = new ConnectorHandler();
		PlaceHandler pTool = new PlaceHandler();
		
		// creo 2 luoghi e un collegamento
		System.out.println( "- Prima città" );
		Place partenza = (Place) pTool.createElement();
		System.out.println( "- Seconda città" );
		Place arrivo = (Place) pTool.createElement();
		System.out.println( "- Collegamento" );
		Connector collegamento = (Connector) cTool.createElement();
		
		// Uso l'handler di Connector per collegare i luoghi
		cTool.connect( collegamento, partenza , arrivo );
		
		// Disegno la mappa finale
		pTool.paintElement( partenza );
		pTool.paintElement( arrivo );
		cTool.paintElement( collegamento );
	}
}
