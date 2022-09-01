
var newman = require('newman'); // require Newman in your project
const fs = require('fs');
const { delay } = require('bluebird');

//SETUP OF PARAMETERS
// const types = ["aws", "azure","gcloud"]
const iterations = 1000
var set = 5
type = "iris"
counter = 4

var datetime = new Date().toISOString()

// for (index in types){
    // var type = types[index]
    const collectionpath = "./"+type+"_collection.json"
    // for(let counter = 0; counter < set; counter++){
        // call newman.run to pass `options` object and wait for callback
        newman.run({
            collection: require(collectionpath),
            reporters: ['cli','json-summary'],
            iterationCount: iterations
        }, function (err) {
            if (err) { throw err; }
            console.log('collection run complete!');
        }).on('request', (error,data) => {
            
            url = data.item.name.split('/')
            fname = url.slice(-1)
            const fileName  = `${fname}-I${iterations}-C${counter}-D${datetime}.txt`
            console.log(fileName)
            const content = data.response.stream.toString()+","
    
            console.log(data.response.stream.toString()+ " - "+ counter)
            
            fs.appendFile(fileName, content, function(error){
                if(error){
                    console.error(error)
                }
            });
        });    
    //    }    
// }
