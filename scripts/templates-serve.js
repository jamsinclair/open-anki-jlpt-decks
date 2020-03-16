#!/usr/bin/env node
'use strict';

const fs = require('fs');
const express = require('express');
const app = express();
const port = 3000;

const questionTemplate = fs.readFileSync('./src/templates/question.html');
const answerTemplate = fs.readFileSync('./src/templates/answer.html');
const styles = fs.readFileSync('./src/templates/styles.css');

const renderCardHtml = content => (`
<!doctype html>
<title>Card</title>
<style>html,body { height: 100%; margin: 0; }</style>
<style>${styles}</style>
<div class="card">${content}</div>
`);

app.get('/question', (req, res) => {
  const content = questionTemplate.toString().replace('{{expression}}', '生きる');
  res.send(renderCardHtml(content));
});

app.get('/answer', (req, res) => {
  const content = answerTemplate.toString().replace('{{expression}}', '生きる')
    .replace('{{reading}}', 'いきる')
    .replace('{{meaning}}', 'to live');
  res.send(renderCardHtml(content));
});

app.listen(port, () => console.log(`Templates app listening on port ${port}!`));