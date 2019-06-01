public class Solution {
    public String countAndSay(int n) {
        if (n <= 1) {
            return "1";
        }
        
        String curr = "1";
        for (int i = 1; i < n; i ++) {
            curr = say(curr);
        }
        
        return curr;
    }
    
    private String say(String value) {
        StringBuilder builder = new StringBuilder();
        
        char character = 0;
        int count = 0;
        for (char c : value.toCharArray()) {
            if (c != character) {
                if (count != 0) {
                    builder.append(String.valueOf(count));
                    builder.append(character);
                }
                character = c;
                count = 1;
            } else {
                count ++;
            }
        }
        
        if (count != 0) {
            builder.append(String.valueOf(count));
            builder.append(character);
        }
        
        return builder.toString();
    }
}