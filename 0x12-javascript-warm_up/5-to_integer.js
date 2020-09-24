#!/usr/bin/node
/* Prints My number: <first argument converted in integer> */

if (!process.argv[2] || isNaN(parseInt(process.argv[2], 10))) {
	console.log('Not a number');
} else {
	console.log('My number:', parseInt(process.argv[2], 10));
}