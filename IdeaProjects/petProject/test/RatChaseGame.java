import Game.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;


public class RatChaseGame extends Dogs {
    Dogs dog;
    LocalDog localDog;
    ProductPurchase product;
    Human human;

    @BeforeEach
    public void instance() {
        dog = new Dogs();
        localDog = new LocalDog();
        product = new ProductPurchase();
        human = new Human("Madison");
    }

    @Test
    void initialDogMoral() {
        dog.dogMoral();
        assertEquals(30, dog.getDogMoral());
    }

    @Test
    void dogBarkMethod() {
        dog.dogBark();
        assertEquals(50, dog.getDogBark());
    }

    @Test
    void dogMoralMethod() {
        dog.dogMoral();
        assertEquals(30, dog.getDogMoral());
    }

    @Test
    void feedDogMethod() {
        dog.dogHealth();
        assertEquals(30, dog.getDogHealth());
    }

    @Test
    void bingoHealthMethodTest() {
        localDog.dogHealth();
        assertEquals(30, localDog.getDogHealth());
    }

    @Test
    void bingoMoralMethodTest() {
        localDog.dogMoral();
        assertEquals(30, localDog.getDogMoral());
    }

    @Test
    void bingoBarkMethodTest() {
        localDog.dogBark();
        assertEquals(50, localDog.getDogBark());
    }
    @Test
    void humanTokenMethodTest(){
        assertEquals(50, human.getToken());
    }
    @Test
    void withdrawToken(){
        human.withdrawToken(5);
        assertEquals(45,human.getToken());
    }
    @Test
    void purchaseLocalDogfoodTwice(){
     int confirm = product.localDogFoodPurchase(2);
     assertEquals(2, confirm);

    }
    @Test
    void purchaseForeignDogFood(){
        assertEquals(3, product.foreignDogFoodPurchase(3));
    }

}
