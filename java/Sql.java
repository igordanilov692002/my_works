package com.example.bd3;

import java.sql.*;
import java.util.ArrayList;
import java.util.Objects;

public class Sql {
    Connection connection = null;
    String url = "jdbc:mysql://localhost:3306/shop";
    String uname = "root";
    String password = "787898asas";

    Sql() {
    }

    public void connect() throws SQLException {
        try {
            // below two lines are used for connectivity.
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            System.out.println("catch_mysql_connect");
            e.printStackTrace();
        }
        try {
            connection = DriverManager.getConnection(url, uname, password);
        } catch (SQLException e) {
            System.out.println("catch_mysql_connect_DriverManager");
            e.printStackTrace();
        }
        System.out.println("sql_connect");
    }

    public Boolean disconnect() throws SQLException {
        try {
            connection.close();
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public String execute(String s) throws SQLException {
        if(s.charAt(s.length() - 1) != ';')
            s += ';';
        if (connection == null)
            return "/нет подключения к бд"; // нет подключения к бд
        try{
            Statement statement = connection.createStatement();
            int rows = statement.executeUpdate(s);
            return "/изменения добавлены";
        } catch(Exception ex) {
            System.out.println(ex);
            return "/не удалось добавить изменения";
        }
    }


    public ArrayList<ArrayList<String>> select(String s) throws SQLException { // доделать
        if (connection == null || Objects.equals(s, ""))
            return new ArrayList<>(); // нет подключения к бд
        if (s.charAt(s.length() - 1) != ';')
            s += ';';
        Statement statement = connection.createStatement();
        ResultSet result = null;
        try {
            result = statement.executeQuery(s);
        } catch (SQLException e) { // неправильный запрос у пользователя
            //e.printStackTrace();
            return null;
        }
        ArrayList<ArrayList<String>> ans = new ArrayList<>();
        try{
            int iter = 0;
            while(result.next()){
                ans.add(new ArrayList<>());
                for(int i = 1; i < 5; i++){
                    try{ // int
                        ans.get(iter).add(result.getString(i));
                    } catch (Exception ignored){}
                }
                iter++;
            }
            return ans;
        } catch (Exception e){
            return new ArrayList<>();
        }
    }
}
