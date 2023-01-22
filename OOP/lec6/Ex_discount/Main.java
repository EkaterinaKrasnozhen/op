public class Main {
    public static void main(String[] args) {
        System.out.println(new BaseClient().getDiscount(100));
        System.out.println(new SilverClient().getDiscount(100));
        System.out.println(new VipClient().getDiscount(100));
    }
}
