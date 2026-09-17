class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() == 0) return 0;
        vector<int> curr(96, 0);

        int l = 0, r = 0;
        curr[s[0] - ' ']++;
        int answer = 1;

        while (r + 1 < s.size()) {
            r += 1;
            curr[s[r] - ' ']++;
            while (curr[s[r] - ' '] > 1) {
                curr[s[l] - ' ']--;
                l++;
            }

            answer = max(answer, r - l + 1);
        }

        return answer;
    }
};
