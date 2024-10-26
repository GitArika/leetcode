function lengthOfLastWord(s: string): number {
  const word = s.trim().split(" ").pop()
  return word?.length || 0
};