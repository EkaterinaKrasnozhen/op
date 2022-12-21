package lec2.TextDoc;

public class TextDocument {
    StringBuilder sb;
    public TextDocument() {
        sb = new StringBuilder();
    }

    public TextDocument(String data) {
        this();
        addAllText(data);
    }

    public void addAllText(String text) {
        sb.append(text + "\n");
    }

    public void addAllines(String [] lines) {
        for (String line : lines) {

        }
    }

    public String getData() {
        return sb.toString();
    }
}
