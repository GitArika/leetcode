function strStr(haystack: string, needle: string): number {
  const re = new RegExp(needle);
  return haystack.search(re);
};