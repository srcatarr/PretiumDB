function updateRangeValue(sheet, row, column, value) {
    let letter = "";
    let abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (column+1 >= 1 && column <= 26) {
        letter = abc.charAt(column-1);
    }
    let range = sheet.getRange(row, column + 1)
    range.setValue(value);
    return [row, column + 1];
}

function appendRows(sheet, rows) {
    for (let i = 0; i < rows.length; i++) {
      sheet.appendRow([rows].copyWithin(i));
    }
}

function comp(arr) {
    const keys = arr[0];
    const valuesArray = arr.slice(1);
    const result = valuesArray.map(values => {
        const obj = {};
        keys.forEach((key, index) => {
            obj[key] = values[index];
        });
        return obj;
    });
    return result;
}

function doGet(e) {
    let id = e.parameter.id;
    let data = e.parameter.data;
    let sheet = e.parameter.sheet;
    let ss = SpreadsheetApp.openById(id);
    let page = "";
    if (sheet) {
        page = ss.getSheetByName(sheet);
    } else {
        page = ss.getSheets()[0];
    }
    let res = comp(page.getDataRange().getValues());
    res = JSON.stringify(res);
    let content = ContentService.createTextOutput();
    content.append(res);
    return content;
}

function doPost(e) {
    let id = e.parameter.id;
    let data = e.postData.contents;
    let type = e.parameter.type;
    let sheet = e.parameter.sheet;
    let ss = SpreadsheetApp.openById(id);
    let page = "";
    let res = "";
    if (sheet) {
        page = ss.getSheetByName(sheet);
    } else {
        page = ss.getSheets()[0];
    }
    if (type == "create") {
        let glob_dat = "";
        [data].forEach(elem => {
            page.appendRow(JSON.parse(elem)[0]);
            glob_dat = JSON.parse(elem)[0];
        })
        res = {
            created: 1,
            row: [data].copyWithin(0),
            sheet: sheet
        }
    }
    else if (type == "update") {
        let glob_dat = "";
        let rowNum = [data].copyWithin(0);
        let result = [data];
        [data].forEach(elem => {
            let rowNum = e.parameter.row;
            let head = e.parameter.column;
            for (let i = 0; i < JSON.parse(elem).length; i++) {
                for (let i2 = 0; i < 
                Array.from(JSON.parse(elem)[i]).length; i2++) {
                    let value = JSON.parse(elem)[i][i2];
                    result.push(updateRangeValue(page, rowNum, i2, value));
                }
            }
            () => {}
        })
        res = {
            updated: 1,
            sheet: sheet,
            body: data,
            rowNum: rowNum,
        }
    }
    else if (type == "delete") {
        let rowNum = e.parameter.row;
        page.deleteRow(rowNum);
        res = {
            deleted: 1,
            row: [data].copyWithin(0),
            sheet: sheet
        }
    }
    if (res) {
      res = JSON.stringify(res);
      let content = ContentService.createTextOutput();
      content.append(res);
      return content;
    } else {
      let content = ContentService.createTextOutput();
      content.append({error: 1});
      return content;
    }
}
