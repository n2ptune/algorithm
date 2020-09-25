const { commandHelp } = require('./template')

function onError(message) {
  console.error(message, commandHelp)
}

module.exports = {
  onError
}
