#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

// Brute force solution O(n^2)
        /*
        std::vector<int> v;
        int i = 0;
        int j = 0;
        int k = nums.size();
        for(i = 0; i < k; i++){
            for (j = 0; j < k; j++){
                if ((i != j) && (nums[i] + nums[j] == target)){
                    std::cout << i << ' ' << j;
                    std::vector<int>::iterator it = v.end();
                    it = v.insert(it, j);
                    it = v.insert(it, i);
                    return v;
                }
            }
        }
        return v;
        */

// O(n) solution
        std::vector<int> v;
        std::map<int, int> m;
        int check;
        for (int i = 0; i<nums.size(); i++)
        {
            check = target - nums[i];
            map<int, int>::const_iterator it = m.find(check);
            if (it != m.end())
            {
                v.push_back(m[check]);
                v.push_back(i);
                return v;
            }
            else
            {
                m[nums[i]] = i;
            }
        }
    }
};

