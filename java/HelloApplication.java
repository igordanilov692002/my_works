package com.example.bd3;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloApplication extends Application {
    //public String main_name;
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(HelloApplication.class.getResource("hello-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 700, 400);
        stage.setTitle("bd3!");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }
}

/*
1)
select t.dt, t.shop_name, t.product_name, t.price, t.number from
(select  purchase.dt as dt, shops.name as shop_name, products.name as product_name,
products.price as price, purchase_products.number as number from
    purchase join purchase_products on purchase.id = purchase_products.purchase_id
    join products on purchase_products.product_id = products.id
    join shops on purchase.shop_id = shops.id) as t;


2)
select t.name, sum(t.number * t.price) from
(select shops.name, purchase_products.number, products.price from
    purchase join purchase_products on purchase.id = purchase_products.purchase_id
    join products on purchase_products.product_id = products.id
    join shops on purchase.shop_id = shops.id) as t
    group by t.name;

3)
use shop;
select t.shop_name, max(t.price), min(t.price), AVG(t.price) from
(select  shops.name as shop_name, products.price as price from
    purchase join purchase_products on purchase.id = purchase_products.purchase_id
    join products on purchase_products.product_id = products.id
    join shops on purchase.shop_id = shops.id) as t
    group by t.shop_name;
 */