class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<Character, Integer> hmapS = new HashMap<>();
        Map<Character, Integer> hmapT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            hmapS.put(s.charAt(i), 1 + hmapS.getOrDefault(s.charAt(i), 0));
            hmapT.put(t.charAt(i), 1 + hmapT.getOrDefault(t.charAt(i), 0));
        }

        return hmapS.equals(hmapT);
    }
}
