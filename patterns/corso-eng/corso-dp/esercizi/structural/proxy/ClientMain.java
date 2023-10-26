package proxy;

public class ClientMain {

	public static void main(String[] args) {

		// CREO il PROXYImpiegato
		// Ottengo l'impiegato con ID=1 --> graziella - 1200 - 12/08/2006
		Impiegato impiegato;
		try {
			impiegato = FactoryImpiegato.getInstance(1);
		
		System.out.println("nome impiegato in memoria è "+impiegato.getNome());
		System.out.println();
		
		// modifico
		System.out.println("eseguo una modifica con lo stesso valore esistente");
		impiegato.setNome("graziella");
		System.out.println("nome impiegato in memoria è "+impiegato.getNome());
		System.out.println();

		// aggiorno il DB, ma la modifica non verrà eseguita 
		System.out.println("aggiorno il DB, ma la modifica non verrà eseguita");
		impiegato.store();
		System.out.println("nome impiegato in memoria è "+impiegato.getNome());
		System.out.println();
		
		// modifico
		System.out.println("eseguo una modifica con nome = romina");
		impiegato.setNome("romina");
		System.out.println();

		//eseguo un rollback
		System.out.println("leggo dal DB, voglio un rollback -> perderò il nuovo nome: romina");
		impiegato.load();
		
		// verifico lo stato dell'oggetto in memoria e sul DB
		System.out.println("nome impiegato in memoria e sul DB è "+impiegato.getNome());

		} catch (ImpiegatoNonTrovatoException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
