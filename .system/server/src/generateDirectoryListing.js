const { sortBySelector } = require('./server-types')
const fixPutSaver = `javascript:((saver) => {
if (typeof saver !== 'number' || saver < 0) return;
$tw.saverHandler.savers[saver].__proto__.uri = function () { return decodeURI(encodeURI(document.location.toString().split('#')[0])); };
$tw.saverHandler.savers[saver] = $tw.modules.types.saver['$:/core/modules/savers/put.js'].exports.create();
})($tw.saverHandler.savers.findIndex(e => e.info.name === 'put'))`;

const info = require('../package.json');

exports.generateDirectoryListing = function (directory) {
    function listEntries(entries) {
        return entries.slice().sort(
            sortBySelector(e => ((e.type === 'folder' ? '0-' : '1-') + e.name.toLocaleLowerCase()))
        ).map((entry, index) => {
            const isFile = ['category', 'folder', 'datafolder', 'error', 'other'].indexOf(entry.type) === -1;
            return 
        }).join("")
    }
    const pathArr = directory.path.split('/').filter(a => a);
    const parentJoin = ["", pathArr.slice(0, pathArr.length - 1).join('/'), ""].join('/');
    const parentPath = parentJoin === '//' ? '/' : parentJoin;
    const name = "Nuun"
    return `
    <!DOCTYPE html>
<html>
<head>
<title>${name}</title>
<link rel="stylesheet" href="/directory.css" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
     <p> Go to <a href="http://127.0.0.1:8888/index">Index page</a></p>
</body>
</html>
`
}