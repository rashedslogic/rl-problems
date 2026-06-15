package leetcode.twosum;

import java.util.HashMap;

class twosum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            int complement = target - num;

            if(seen.containsKey(complement)){
                return new int[] {i, seen.get(complement)};
            }

            seen.put(num, i);
        }

        return new int[] {};
    }
}