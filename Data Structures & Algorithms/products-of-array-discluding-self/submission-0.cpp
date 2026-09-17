class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix(n, 1);
        vector<int> suffix(n, 1);

        for (int i = 0; i < n - 1; i++) {
            prefix[i + 1] = prefix[i] * nums[i];
        }
        for (int i = n - 1; i > 0; i--) {
            suffix[i - 1] = suffix[i] * nums[i];
        }

        // for (int i : prefix) cout << i << " ";
        // cout << endl;
        // for (int j : suffix) cout << j << " ";
        // cout << endl;

        vector<int> answer(n, 0);
        for (int i = 0; i < n; i++) {
            answer[i] = prefix[i] * suffix[i];
        }
        return answer;
    }
};
