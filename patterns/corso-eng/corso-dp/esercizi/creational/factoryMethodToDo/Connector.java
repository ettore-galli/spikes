package factoryMethodToDo;

public class Connector implements MapElement {

	private String connectorLabel;
	private Place place1, place2;
	
	public void setLabel( String label ) {
		connectorLabel = label;
	}
	
	public void setPlacesConnected( Place origin, Place destination ) {
		place1 = origin;
		place2 = destination;
	}
	
	public String getPaintingData() {
		return "["+place1.getPaintingData() +" "+ connectorLabel +" "+ place2.getPaintingData() + "]";
	}
}
