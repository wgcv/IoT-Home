const https = require('https');
var AWS = require('aws-sdk');
var domain = process.env.url;
var username = 'XXXXX'
exports.handler = function (request, context) {
    if (request.directive.header.namespace === 'Alexa.Discovery' && request.directive.header.name === 'Discover') {
        handleDiscovery(request, context, "");
    }
    else if (request.directive.header.namespace === 'Alexa.PowerController') {
        if (request.directive.header.name === 'TurnOn' || request.directive.header.name === 'TurnOff') {
            handlePowerControl(request, context);
        }
    }
    else if (request.directive.header.namespace === 'Alexa.StepSpeaker') {
        if (request.directive.header.name === 'AdjustVolume') {
            handleAdjustVolumel(request, context);
        }
        else  if (request.directive.header.name === 'SetMute') {
            handleMutel(request, context);
        }
    }
    else if (request.directive.header.namespace === 'Alexa.InputController') {
        if (request.directive.header.name === 'SelectInput') {
            handleSelectInput(request, context);
        }
        
    }

    function handleDiscovery(request, context) {
        var payload = {
            "endpoints":
            [
                {
                    "endpointId": "Doppio Tv",
                    "manufacturerName": "Smart Tv by Gustavo Cevallos",
                    "friendlyName": "Gustavo Tv",
                    "description": "Smart Tv Device",
                    "displayCategories": ["TV"],
                    "cookie": {
                        "key1": "arbitrary key/value pairs for skill to reference this endpoint.",
                    },
                    "capabilities":
                    [
                        {
                          "type": "AlexaInterface",
                          "interface": "Alexa",
                          "version": "3"
                        },
                        {
                            "interface": "Alexa.PowerController",
                            "version": "3",
                            "type": "AlexaInterface",
                            "properties": {
                                "supported": [{
                                    "name": "powerState"
                                }],
                                 "retrievable": true
                            }
                        },
                         {
                            "interface": "Alexa.StepSpeaker",
                            "version": "3",
                            "type": "AlexaInterface",
                            "properties": {
                                "supported": [{
                                    "name": "mute"
                                },
                                {
                                    "name": "volumeSteps"
                                }],
                                 "retrievable": true
                            }
                        },
                         {
                            "interface": "Alexa.InputController",
                            "version": "3",
                            "type": "AlexaInterface",
                            "properties": {
                                "supported": [{
                                    "name": "TV"
                                },
                                {
                                    "name": "IPOD"
                                },
                                {
                                  "name":"HDMI 1"  
                                },
                                {
                                  "name":"HDMI 2"  
                                },
                                {
                                  "name":"AUX 1"  
                                },
                                {
                                  "name":"AUX 2"  
                                },
                                {
                                  "name":"VIDEO 1"  
                                },
                                {
                                  "name":"VIDEO 2"  
                                }],
                                 "retrievable": true
                            }
                        }
                    ]
                }
            ]
        };
        var header = request.directive.header;
        header.name = "Discover.Response";
        log("DEBUG", "Discovery Response: ", JSON.stringify({ header: header, payload: payload }));
        context.succeed({ event: { header: header, payload: payload } });
    }

    function log(message, message1, message2) {
        console.log(message + message1 + message2);
    }

    function  handlePowerControl(request, context){
        // get device ID passed in during discovery
        var requestMethod = request.directive.header.name;
        var responseHeader = request.directive.header;
        responseHeader.namespace = "Alexa";
        responseHeader.name = "Response";
        responseHeader.messageId = responseHeader.messageId + "-R";
        // get user token pass in request
        var requestToken = request.directive.endpoint.scope.token;
        var powerResult;
        var url = 'tvdoppio/power'

        var contextResult = {
            "properties": [{
                "namespace": "Alexa.PowerController",
                "name": "powerState",
                "value": "OFF",

            }]
        };
        var response = {
            context: contextResult,
            event: {
                header: responseHeader,
                endpoint: {
                    scope: {
                        type: "BearerToken",
                        token: requestToken
                    },
                    endpointId: "demo_id"
                },
                payload: {}
            }
        };
        console.log('https://'+domain+'/'+url+'?username=' + username)
         https.get('https://'+domain+'/'+url+'?username=' + username, (resp) => {
        context.succeed(response);
console.log('ok')
            }).on("error", (err) => {
            console.log("Error: " + err.message);
        });
    }
    function handleAdjustVolumel(request, context) {
        // get device ID passed in during discovery
        var requestMethod = request.directive.header.name;
        var responseHeader = request.directive.header;
        responseHeader.namespace = "Alexa";
        responseHeader.name = "Response";
        responseHeader.messageId = responseHeader.messageId + "-R";
        // get user token pass in request
        var requestToken = request.directive.endpoint.scope.token;
        var powerResult;
        var volumeSteps = request.directive.payload.volumeSteps;
        var url = 'tvdoppio/volume/';
        if(volumeSteps<0){
            url = url + 'down';
        }else{
            url = url + 'up';
        }
        

        var contextResult = {
            "properties": [{
                "namespace": "Alexa.StepSpeaker",
                "name": "AdjustVolume",
                "value": volumeSteps
            }]
        };
        var response = {
            context: contextResult,
            event: {
                header: responseHeader,
                endpoint: {
                    scope: {
                        type: "BearerToken",
                        token: requestToken
                    },
                    endpointId: "demo_id"
                },
                payload: {}
            }
        };
         https.get('https://'+domain+'/'+url+'?username='+username, (resp) => {
        context.succeed(response);

            }).on("error", (err) => {
            console.log("Error: " + err.message);
        });
    }
    

    function handleMutel(request, context) {
        // get device ID passed in during discovery
        var requestMethod = request.directive.header.name;
        var responseHeader = request.directive.header;
        responseHeader.namespace = "Alexa";
        responseHeader.name = "Response";
        responseHeader.messageId = responseHeader.messageId + "-R";
        // get user token pass in request
        var requestToken = request.directive.endpoint.scope.token;
        var powerResult;
        var url = 'tvdoppio/mute'

        var contextResult = {
            "properties": [{
                "namespace": "Alexa.StepSpeaker",
                "name": "mute",
                "value": true,
            }]
        };
        var response = {
            context: contextResult,
            event: {
                header: responseHeader,
                endpoint: {
                    scope: {
                        type: "BearerToken",
                        token: requestToken
                    },
                    endpointId: "demo_id"
                },
                payload: {}
            }
        };
         https.get('https://'+domain+'/'+url+'?username='+username, (resp) => {
        context.succeed(response);

            }).on("error", (err) => {
            console.log("Error: " + err.message);
        });
    }
function handleSelectInput(request, context) {
        // get device ID passed in during discovery
        var requestMethod = request.directive.header.name;
        var responseHeader = request.directive.header;
        responseHeader.namespace = "Alexa";
        responseHeader.name = "Response";
        responseHeader.messageId = responseHeader.messageId + "-R";
        // get user token pass in request
        var requestToken = request.directive.endpoint.scope.token;
        var powerResult;
        var input = request.directive.payload.input;
        var url = 'tvdoppio/';
        if(input== 'IPOD'){
            url = url + 'sleep';
        }else{
            url = url + 'input';
        }
        

        var contextResult = {
            "properties": [{
                "namespace": "Alexa.InputController",
                "name": "SelectInput",
                "value": input
            }]
        };
        var response = {
            context: contextResult,
            event: {
                header: responseHeader,
                endpoint: {
                    scope: {
                        type: "BearerToken",
                        token: requestToken
                    },
                    endpointId: "demo_id"
                },
                payload: {}
            }
        };
         https.get('https://'+domain+'/'+url+'?username='+username, (resp) => {
        context.succeed(response);

            }).on("error", (err) => {
            console.log("Error: " + err.message);
        });
    }
};
