fs = require "fs"

for i in [1..26]
    fs.writeFileSync "10-#{i}.py"