#!/usr/bin/env node
'use strict'

const puppeteer = require('puppeteer')

const init = async () => {
  const browser = await puppeteer.launch()
  const page = await browser.newPage()
  await page.setViewport({
    width: 320,
    height: 350,
    deviceScaleFactor: 1
  })
  await page.goto('http://localhost:3000/question')
  await page.screenshot({ path: 'screenshots/question.png' })
  await page.goto('http://localhost:3000/answer')
  await page.screenshot({ path: 'screenshots/answer.png' })
  await browser.close()
}

init()
