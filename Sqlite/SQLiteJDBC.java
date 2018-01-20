import java.sql.*;

public class SQLiteJDBC
{
  public static void main( String args[] )
  {
    Connection c = null;
    Statement stmt=null;
    try {
      Class.forName("org.sqlite.JDBC");
      c = DriverManager.getConnection("jdbc:sqlite:test.db");

    System.out.println("Opened database successfully");

	stmt=c.createStatement();
	ResultSet rs=stmt.executeQuery("SELECT * FROM DATA WHERE rowid=(Select max(rowid) from DATA)");
	
		String T=rs.getString("TIME");
		System.out.println("T="+T);
	
	rs.close();
	stmt.close();
	c.close();
	    } catch ( Exception e ) {
      System.err.println( e.getClass().getName() + ": " + e.getMessage() );
      System.exit(0);
    }

  }
}

