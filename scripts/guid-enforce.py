#!/usr/bin/env python3
import csv
import genanki
import os
import sys

csvFiles = [
    "src/n5.csv",
    "src/n4.csv",
    "src/n3.csv",
    "src/n2.csv",
    "src/n1.csv",
]


def findMissingGuids(csvPath, callback, overwrite):
    newCsv = []
    hasChangedData = False
    with open(csvPath, mode="r", newline="") as csvFile:
        reader = csv.reader(csvFile)
        lineCount = 0
        for row in reader:
            if lineCount > 0 and row[4].strip() == "":
                newRow = callback(row, lineCount)
                if newRow != None:
                    hasChangedData = True
                    newCsv.append(newRow)
                else:
                    newCsv.append(row)
            else:
                newCsv.append(row)
            lineCount += 1
    csvFile.close()
    if overwrite and hasChangedData:
        with open(csvPath, "r+", newline="") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(newCsv)

            # Remove trailing newline from end of file
            csvFile.seek(0)
            content = csvFile.read()
            content = content.rstrip()
            csvFile.seek(0)
            csvFile.write(content)
            csvFile.truncate()
            csvFile.close()
        csvFile.close()


def checkForMissingGuids(csvPath):
    ctx = {
        "hasMissingGuids": 0,
    }

    def callback(row, lineCount):
        ctx["hasMissingGuids"] = 1
        print("Missing guid on line " + str(lineCount + 1) + " of " + csvPath)
        print(row)

    findMissingGuids(csvPath, callback, False)
    return ctx["hasMissingGuids"]


def fixMissingGuids(csvPath):
    def callback(row, lineCount):
        newRow = row.copy()
        newRow[4] = genanki.guid_for(row[0], row[1], row[2])
        print("Fixed guid on line " + str(lineCount + 1) + " of " + csvPath)
        return newRow

    findMissingGuids(csvPath, callback, True)


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else ""

    if command == "check" or command == "":
        hasMissingGuids = False
        for csvPath in csvFiles:
            result = checkForMissingGuids(csvPath)
            if result == 1:
                hasMissingGuids = True
        if hasMissingGuids:
            print("Missing guids found in one or more csv files")
            print("Run `scripts/guid-enforce.py fix` to fix them")
            sys.exit(1)
        sys.exit(0)

    if command == "fix":
        for csvPath in csvFiles:
            fixMissingGuids(csvPath)
        sys.exit(0)

    print("Unknown command: " + command)
    sys.exit(1)
