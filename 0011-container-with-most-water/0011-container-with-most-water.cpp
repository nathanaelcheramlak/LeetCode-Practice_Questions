class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max_area = 0;
        
        while (right > left) {
            int h = min(height[left], height[right]);
            int width = right - left;
            int current_area = h * width;
            
            max_area = max(max_area, current_area);
            
            if (height[right] > height[left])
                left++;
            else
                right--;
        }
        return max_area;
    }
};