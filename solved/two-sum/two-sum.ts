function twoSum(nums: number[], target: number): number[] {
  const numMap = new Map();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];

    if (numMap.has(complement)) {
      return [numMap.get(complement), i];
    }

    numMap.set(nums[i], i);
  }

  return [];
}