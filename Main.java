import java.util.HashMap;
import java.util.Map;

/**
 * Main
 */
public class Main {

    public static void main(String[] args) {
        Map<String, Integer> persona = new HashMap<>();
        persona.put("Maria", 26);
        persona.put("Elon", 85);
        persona.put("Noemi", 35);
        for (Map.Entry<String, Integer> entry: persona.entrySet()) {
            System.out.println("Nombre: " + entry.getKey() + ", Edad: " + entry.getValue());
        }
    } 
}