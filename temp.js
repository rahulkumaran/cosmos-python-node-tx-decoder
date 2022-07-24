const {createDefaultRegistry, defaultRegistryTypes : defaultStargateTypes, SigningStargateClient} = require("@cosmjs/stargate") ;
const {decodeTxRaw} = require("@cosmjs/proto-signing");
const {Registry} = require("@cosmjs/proto-signing");

const {fromBase64} = require("@cosmjs/encoding");

const registry = new Registry(defaultStargateTypes)


const parseTx = (tx) => {
    const decoded = decodeTxRaw(fromBase64(tx));
    const parsedData = [];
    //console.log(decoded.body)
    for (const message of decoded.body.messages) {
        console.log(message.typeUrl + ",") 
        const decodedMsg = registry.decode(message);
        console.log(decodedMsg)
        parsedData.push(decodedMsg);
    }
    return parsedData;
};

parseTx(process.argv[2])