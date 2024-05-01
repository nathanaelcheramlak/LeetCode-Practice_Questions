class Solution {
public:
    string reversePrefix(string word, char ch) {
        int index = 0;
        // Check if the character exists in the word.
        for (int i = 0; i < word.size(); i++) {
            if (word[i] == ch)
            {
                index = i;
                break;
            }
        }
        
        int p1 = 0;
        int p2 = index;
        
        while (p2 >= p1)
        {
            char temp = word[p1];
            word[p1] = word[p2];
            word[p2] = temp;
            
            p1++;
            p2--;
        }
        
        return word;
    }
};