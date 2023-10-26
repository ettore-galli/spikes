package proxy;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Locale;
import java.util.ResourceBundle;

public class DaoImpiegato {

	private Connection conn;
	
	public DaoImpiegato(){
		try {
			ResourceBundle risorse =ResourceBundle.getBundle("proxy.mio", Locale.getDefault());
			String driver= risorse.getString("nome.driver");
			String connessione= risorse.getString("nome.connessione");
			
			Class.forName(driver);
			this.conn = DriverManager.getConnection(connessione);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	public void update(Impiegato i){
		
		try {
			PreparedStatement st = conn.prepareStatement("update impiegato set nome=?,assunzione=?,salario=? where id=?");
			st.setString(1, i.getNome());
			st.setString(2, i.getAssunzione());
			st.setDouble(3, i.getSalario());
			st.setInt(4, i.getId());
			st.executeUpdate();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	public Impiegato select(String condition) throws ImpiegatoNonTrovatoException{
		ImpiegatoImpl imp=null;
		try {
			PreparedStatement st = conn.prepareStatement("select * from impiegato "+condition);
			ResultSet rs = st.executeQuery();
			
			if(rs.next())
			{
				imp = new ImpiegatoImpl(rs.getString("nome"),rs.getDouble("salario"),rs.getString("assunzione"),rs.getInt("id"));
			}
			else
				throw new ImpiegatoNonTrovatoException("impiegato non trovato");
			
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
		return imp;
	}	
	
	public void closeConn()
	{
		try {
			this.conn.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
}
