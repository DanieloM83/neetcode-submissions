class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> curr(128, 0);

        int l = 0;
        int answer = 0;

        for (int r = 0; r < s.size(); r++) {
            curr[s[r]]++;

            while (curr[s[r]] > 1) {
                curr[s[l]]--;
                l++;
            }

            answer = max(answer, r - l + 1);
        }

        return answer;
    }
};
