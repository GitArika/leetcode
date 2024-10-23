function getRomanMap(): Map<string, number> {
  const roman = new Map();

  roman.set('I', 1);
  roman.set('V', 5);
  roman.set('X', 10);
  roman.set('L', 50);
  roman.set('C', 100);
  roman.set('D', 500);
  roman.set('M', 1000);
  roman.set('IV', 4);
  roman.set('IX', 9);
  roman.set('XL', 40);
  roman.set('XC', 90);
  roman.set('CD', 400);
  roman.set('CM', 900);

  return roman;
}

// s = MCMXCIV = 1994
function romanToInt(s: string): number {
  const roman = getRomanMap();

  const iterable = s.split("");
  let sum = 0

  for (let i = 0; i < iterable.length; i++) {
    if (roman.has(iterable[i] + iterable[i + 1])) {
      sum += roman.get(iterable[i] + iterable[i + 1]);
      i++;
      continue;
    } else {
      sum += roman.get(iterable[i]);
      continue;
    }
  }

  return sum
};