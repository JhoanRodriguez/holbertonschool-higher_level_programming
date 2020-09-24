#!/usr/bin/node
/* Handling argv, argc */

if (process.argv.length < 3) {
	console.log('No argument');
} else if (process.argv.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}