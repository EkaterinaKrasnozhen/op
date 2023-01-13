package lec5.ContactBook;


public class Contact {
    
    private String firstName;
    private String lastName;
    private int id;
    private String phone;

    


    public Contact(int id, String firstName, String lastName, String phone) {
        this.id = ++id;
        this.firstName =firstName;
        this.lastName = lastName;
        this.phone = phone;
    }

    public int getId() {
        return id;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setId(int id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "id: " + id + ", FirstName: " + firstName + ", LastName: " + lastName + ", Phone: " + phone;
    }

}
