#!/usr/bin/env node
'use strict'

const puppeteer = require('puppeteer')

const init = async () => {
  const browser = await puppeteer.launch()
  const page = await browser.newPage()
  await page.setViewport({
    width: 320,
    height: 350,
    deviceScaleFactor: 2
  })
  await page.goto('http://localhost:3000/en/question')
  await page.screenshot({ path: 'screenshots/en-question.png' })
  await page.goto('http://localhost:3000/en/answer')
  await page.screenshot({ path: 'screenshots/en-answer.png' })
  await page.goto('http://localhost:3000/jp/answer')
  await page.screenshot({ path: 'screenshots/jp-answer.png' })
  await page.goto('http://localhost:3000/jp/question')
  await page.screenshot({ path: 'screenshots/jp-question.png' })
  await browser.close()
}

init()
