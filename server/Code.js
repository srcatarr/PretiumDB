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
        ss.getRange().setValue();
    }
    else if (type == "delete") {
        let rowNum = e.parameter.row;
        page.deleteRow(rowNum);
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
