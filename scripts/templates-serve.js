#!/usr/bin/env node
'use strict'

const fs = require('fs')
const express = require('express')
const app = express()
const port = 3000

const questionTemplates = {
  en: fs.readFileSync('./src/templates/en-question.html').toString(),
  jp: fs.readFileSync('./src/templates/jp-question.html').toString()
}
const answerTemplates = {
  en: fs.readFileSync('./src/templates/en-answer.html').toString(),
  jp: fs.readFileSync('./src/templates/jp-answer.html').toString()
}
const styles = fs.readFileSync('./src/templates/styles.css')

const renderFields = content => {
  return content
    .replace('{{expression}}', '生きる')
    .replace('{{meaning}}', 'to live')
    .replace('{{reading}}', 'いきる')
}

const renderCardHtml = content => `
<!doctype html>
<title>Card</title>
<style>html,body { height: 100%; margin: 0; }</style>
<style>${styles}</style>
<div class="card">${renderFields(content)}</div>
`
app.get('/en/question', (req, res) => {
  res.send(renderCardHtml(questionTemplates.en))
})

app.get('/en/answer', (req, res) => {
  res.send(renderCardHtml(answerTemplates.en))
})

app.get('/jp/question', (req, res) => {
  res.send(renderCardHtml(questionTemplates.jp))
})

app.get('/jp/answer', (req, res) => {
  res.send(renderCardHtml(answerTemplates.jp))
})

app.listen(port, () => console.log(`Templates app listening on port ${port}!`))
