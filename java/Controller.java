package com.example.bd3;

import java.net.URL;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;

public class Controller {
    Sql sql = new Sql();

    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private TextArea TextArea_out;

    @FXML
    private Button btn_connect;

    @FXML
    private Button btn_disconect;

    @FXML
    private Button btn_exec;

    @FXML
    private Button btn_select;

    @FXML
    private TextField textArea_input;

    @FXML
    void initialize() {
        btn_connect.setOnAction(event -> {
            String s = "/успешное подключение к db";
            try {
                sql.connect();
            } catch (SQLException e) {
                s = "/не удалось подключиться к db";
            }
            TextArea_out.clear();
            TextArea_out.setText(s);
        });


        btn_exec.setOnAction(event -> {
            String s;
            try {
                s = sql.execute(textArea_input.getText());
            } catch (SQLException e) {
                s = "/непредвиденная ошибка";
            }
            TextArea_out.clear();
            TextArea_out.setText(s);
            textArea_input.clear();
        });


        btn_select.setOnAction(event -> {
            TextArea_out.clear();
            try {
                ArrayList<ArrayList<String>> ans = sql.select(textArea_input.getText());
                if(ans == null || ans.isEmpty()) {
                    TextArea_out.setText("/не сработало");
                }
                String s = "";
                for(int i = 0;i < ans.size();i++){
                    for(int i1 = 0;i1 < ans.get(i).size();i1++){
                        s += ans.get(i).get(i1) + '\t';
                    }
                    s += System.lineSeparator();
                }
                TextArea_out.setText(s);
            } catch (SQLException e) {
                TextArea_out.setText("/не сработало");
            }
            textArea_input.clear();
            System.out.println("btn_select");

        });


        btn_disconect.setOnAction(event -> {
            TextArea_out.clear();
            try {
                if(sql.disconnect())
                    TextArea_out.setText("/отключение от бд");
                else
                    TextArea_out.setText("/не удалось отключиться от бд");
            } catch (SQLException e) {
                TextArea_out.setText("/не удалось отключиться от бд");
            }
        });
    }

}