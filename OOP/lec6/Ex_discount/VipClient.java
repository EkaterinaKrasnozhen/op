public class VipClient extends SilverClient {
    @Override
    public double getDiscount(double price) {
        return super.getDiscount(price) * 0.9;
    }
}
