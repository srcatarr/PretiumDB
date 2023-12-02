// Setting constant & environment variables

ScriptProperties.setProperty("result", "");

// Functions of request

function doGet(e:any) {
    if (e.parameter.req == "get") {
        get();
    }
}
function doPost(e:any) {}

// Setting request properties

const ss:any = SpreadsheetApp.openById(
    String(
        ScriptProperties.getProperty("SPREADSHEET_ID")
    )
);
const ssp:any = ss.getSheetByName(
    String(
        ScriptProperties.getProperty("SHEET_NAME")
    )
);
const vals:any = ssp?.getDataRange().getValues();

SpreadsheetApp.openById("").getSheetByName("")?.appendRow([]);

// Functions for server

function get() :void /* The function of get data */ {
    for ( let i:number = 0; i <= vals.length; i++ ) {
        if ( i !== 0 ) {
            let obj:any = vals[i];
            let query:any = obj[0];
            let properties:any = vals[0];
            for ( let x:number = 0; x <= properties.length; x++ ) {
                let result:any = ScriptProperties.getProperty("result");
                result[query][properties[x+1]] = obj[x+1];
                ScriptProperties.setProperty("result", result);
            }
        }
    }
}
function set(query:string, property:string, val:string) :void /* The function of set data */ {
    let properties:any = vals[0];
    vals.forEach(obj => {
        if ( obj[0] == query ) {
            for ( let i:number = 0; i <= properties.length; i++ ) {
                if ( properties[i] == property ) {
                    vals[query][property] = val;
                    return true;
                }
            }
        }
    });
}

function appendRow(row:any[]) :void /* The function of appending row */ {
    ssp?.appendRow(row);
}
