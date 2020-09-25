const tableTemplate = `| Time Submmited | Status | Runtime | Memory | Language |
| --- | --- | --- | --- | --- |
| - | - | - | - | - |

##`

const commandHelp = `

===============================================================
Command   Property  Value             Required  Default

gen:md    level     easy,medium,hard  true      -
          title     [string]          false     default.md
===============================================================

`

module.exports = {
  tableTemplate,
  commandHelp
}
