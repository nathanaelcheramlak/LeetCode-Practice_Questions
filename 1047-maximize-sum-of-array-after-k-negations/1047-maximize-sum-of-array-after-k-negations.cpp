class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        for (auto& num : nums) {
            if (num > 0 || k == 0) break;
            num *= -1;
            k -= 1;
        }
        int sum = accumulate(nums.begin(), nums.end(), 0);
        return k & 1 ? sum - 2 * *min_element(nums.begin(), nums.end()) : sum;
    }
};