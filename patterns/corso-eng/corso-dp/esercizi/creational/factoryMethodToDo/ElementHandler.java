package factoryMethodToDo;

import java.io.*;
public abstract class ElementHandler {
	
	public MapElement createElement( ) throws IOException {
		BufferedReader reader = new BufferedReader( new InputStreamReader(System.in) );
		System.out.println( "Inserisci nome o simbolo per l'elemento da creare: ");
		String label = reader.readLine();
		MapElement element = newElement( );
		element.setLabel( label );
		return element;
	}

	protected abstract MapElement newElement();
	
	public void paintElement(MapElement element) {
		System.out.println( element.getPaintingData() );
	}
}
