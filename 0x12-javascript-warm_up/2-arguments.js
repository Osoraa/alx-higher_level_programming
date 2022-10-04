#!/usr/bin/node
import { argv } from 'node:process';

if (len(argv) <= 2){
    console.log('No argument');
} else if (len(argv) == 3){
    console.log('Argumnt found');
} else {
    console.log('Arguments found')
}

