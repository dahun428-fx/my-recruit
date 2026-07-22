const vscode = require('vscode');
const http = require('http');

const PORT = 27183;
let server;

function json(response, status, body) {
  response.writeHead(status, { 'Content-Type': 'application/json' });
  response.end(JSON.stringify(body));
}

async function findTerminalByPid(pid) {
  for (const terminal of vscode.window.terminals) {
    if (await terminal.processId === pid) {
      return terminal;
    }
  }
  return undefined;
}

function startServer() {
  server = http.createServer((request, response) => {
    if (request.method !== 'POST' || request.url !== '/continue') {
      return json(response, 404, { error: 'Not found' });
    }

    let raw = '';
    request.setEncoding('utf8');
    request.on('data', (chunk) => { raw += chunk; });
    request.on('end', async () => {
      try {
        const body = JSON.parse(raw);
        const pids = [...new Set(body.pids)].map(Number);
        if (!Array.isArray(body.pids) || pids.some((pid) => !Number.isInteger(pid) || pid <= 0)) {
          return json(response, 400, { error: 'pids must be an array of positive integers' });
        }

        const results = [];
        for (const pid of pids) {
          const terminal = await findTerminalByPid(pid);
          if (!terminal) {
            results.push({ pid, sent: false, reason: 'terminal not found' });
            continue;
          }

          terminal.sendText('계속해', true);
          results.push({ pid, sent: true, terminal: terminal.name });
        }

        return json(response, 200, { results });
      } catch (error) {
        return json(response, 400, { error: error.message });
      }
    });
  });

  server.listen(PORT, '127.0.0.1');
}

function activate(context) {
  startServer();
  context.subscriptions.push({
    dispose: () => server?.close(),
  });
}

function deactivate() {
  server?.close();
}

module.exports = { activate, deactivate };
