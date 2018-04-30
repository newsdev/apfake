const path = require("path")
const { spawn } = require("child_process")

const dockerFilePath = path.resolve(__dirname, "docker-compose.yml")

const { FILE, DATE, PATH } = process.env

if (!FILE || !DATE) {
  throw Error(`You must set FILE and DATE environment variables.`)
}

const proc = spawn("docker-compose", ["--file", dockerFilePath, "up"])
proc.stdout.pipe(process.stdout)
proc.stderr.pipe(process.stderr)