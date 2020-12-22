const { join } = require('path')

const root = join(__dirname, '../../')
const problems = join(root, 'problems/')
const rootReadme = join(root, 'README.md')

module.exports = {
  path: {
    root,
    problems,
    rootReadme
  }
}
