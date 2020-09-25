const levelWrap = process.argv.filter((item) => item.startsWith('level'))[0]
const titleWrap = process.argv.filter((item) => item.startsWith('title'))[0]
const { onError } = require('./error')

if (!levelWrap) {
  return onError('The level is required and must be one of Easy, Medium, and Hard.')
}

const level = levelWrap.split('=')[1]
const title = titleWrap ? titleWrap.split('=')[1] + '.md' : 'default.md'

switch (level) {
  case 'easy':
  case 'medium':
  case 'hard':
    break
  default:
    throw new Error(
      'The level is required and must be one of Easy, Medium, and Hard.'
    )
}

const fs = require('fs')
const path = require('path')
const problemPath = path.resolve(__dirname, '../', '../', 'problems', level)
const prettier = require('prettier')
const { tableTemplate: template } = require('./template')

const lintedStructure = prettier.format(template, { parser: 'markdown' })

try {
  if (!fs.existsSync(problemPath)) {
    fs.mkdirSync(problemPath)
  }

  fs.writeFileSync(`${problemPath}/${title}`, lintedStructure, {
    flag: 'w',
    encoding: 'utf-8'
  })
} catch (error) {
  throw new Error(error)
} finally {
  return console.log(`Success generated markdown file into ${problemPath}`)
}
