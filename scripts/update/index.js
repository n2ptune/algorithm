const { path } = require('../constants')
const fs = require('fs')

function update() {
  const text = fs
    .readFileSync(path.rootReadme, { encoding: 'utf-8' })
    .split('\n')

  const startIndex = text.findIndex((t) => t === '### Leetcode')
  const endIndex =
    text.findIndex((t) => t === '', text.slice(startIndex)) + startIndex + 1

  if (startIndex === -1) {
    throw new Error('Leetcode 부분을 찾을 수 없음')
  }

  text.splice(startIndex, endIndex)
}

update()
