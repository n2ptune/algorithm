let sum = 0

require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .split('\n')
  .slice(1)
  .forEach((input) => {
    const parse = input.split(' ').map((s) => parseInt(s))
    const r = [...new Set(parse)]

    let ans = 0

    if (r.length === 3) {
      ans = Math.max(r) * 100
    } else if (r.length === 2) {
      const max = Math.max(r)
      const s = parse.filter((a) => a === max)
      const m = s.length > 1 ? max : Math.min(r)
      ans = 1000 + m * 100
    } else {
      ans = 10000 + Math.max(r) * 1000
    }

    sum = ans >= sum ? ans : sum
  })

console.log(sum)
