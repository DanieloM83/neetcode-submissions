class Solution {
public:

    string encode(vector<string>& strs) {
        string res;
        for (string& s : strs) {
            res.append(to_string(s.size()));
            res.push_back('#');
            res.append(s);
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int l = 0;
        while (l < s.size()) {
            int r = l;
            while (s[r] != '#') {
                r++;
            }
            int len = stoi(s.substr(l, r - l)); // length of the string

            l = r + 1; // start of the string
            r = l + len; // end of the string, start of the next string length
            res.push_back(s.substr(l, len));
            l = r;
        }
        return res;
    }
};
