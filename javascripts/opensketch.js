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
            dialog("/?_id=" + responseData._id);
        })
        .error(function(responseData, textStatus, error) {
            console.log(error); 
        })
        /* do not need complete function here
        .complete(function(responseData, textStatus ) {
            //dialog("/?_id=" + responseData._id);
        });
        */

	},

	/**
	 * Function to load a sketch
	 */
	this.load = function() {
        //$.getJSON( url [, data ] [, success(data, textStatus, jqXHR) ] )
	}

};//(window.opensketch);
