/*
 * Opensketch
 * Version 0.0.1
 */


var opensketch = function() {
//(var opensketch = function() {

	/**
	 * Function to save a sketch, returns a link
	 */
	this.save = function(url, data, dialog) {

        var responseData = null;

        $.ajax({
            url: url,
            type: 'GET', // PUT not supported
            dataType: 'jsonp',
            jsonp: 'callbackFunc',
            data: {'sketchText': data}
        })
        .success(function(responseData, textStatus ) {
            dialog("/?oid=" + responseData._id);
        })
        .error(function(responseData, textStatus, error) {
            console.log(error); 
        })

	},

	/**
	 * Function to load a sketch
	 */
	this.load = function(url, data, sketchpad) {
        var responseData = null;

        $.ajax({
            url: url,
            type: 'GET', // PUT not supported
            dataType: 'jsonp',
            jsonp: 'callbackFunc',
            data: {'oid': data}
        })
        .success(function(responseData, textStatus ) {
            sketchTextJSON = JSON.parse(responseData.sketchText);
            sketchpad.strokes(sketchTextJSON);
        })
        .error(function(responseData, textStatus, error) {
            console.log(error); 
        })

	}

};
