class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> all = new ArrayList<>();
        dfs(0, nums, all, new ArrayList<Integer>());
        return all;
    }

    private void dfs(int idx, int[] nums, List<List<Integer>> allSubsets, List<Integer> curSubset) {
        
        if (idx >= nums.length) {
            allSubsets.add(new ArrayList<>(curSubset));
            return;
        }

        curSubset.add(nums[idx]);
        dfs(idx + 1, nums, allSubsets, curSubset);
        curSubset.remove(curSubset.size() - 1);

        while (idx < nums.length - 1 && nums[idx] == nums[idx+1]) {
            idx++;
        }

        dfs(idx + 1, nums, allSubsets, curSubset);


    }
}
