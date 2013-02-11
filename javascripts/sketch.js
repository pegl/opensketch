/**
 * sketch.js
 *
 * javascript function for sketch.html
 *
 * On loading, check request args
 * If oid exists, try to load the drawing from api
 * set the sketchpad json directly/refresh drawing
 *
*/

$(function() {

    var getParameterInt = function(param) {
        var val = document.URL;
        var url = val.substr(val.indexOf(param))  
        var n=parseInt(url.replace(param+"=",""));
        return n; 
    }

    /*THIS FUNCTION IS TO FETCH STRING PARAMETER*/
    var getParameter = function(param) {
        var val = document.URL;
        var url = val.substr(val.indexOf(param))  
        var n=url.replace(param+"=","");
        return n; 
    }

    var oid = getParameter("oid") 
    if (oid.length > 0) {
        var os = new opensketch();
        os.load(os.loadURI, oid, sketchpad);
    }

});

/*
         * On clicking share, send request to persist and build the link
*/

// configurable host
if (!window.location.origin) window.location.origin = window.location.protocol+"//"+window.location.host;

    $(function() {
        $( "input[type=submit][value=New]" )
        .button()
        .click(function( event ) {
            event.preventDefault();
            sketchpad.clear();
        })
    });

    $(function() {
        $( "input[type=submit][value=Save]" )
        .button()
        .click(function( event ) {
            event.preventDefault();
            var os = new opensketch();
            var sketchText = sketchpad.json();
            os.save(os.saveURI, sketchText, dialog);
        });
    });

    var shareLink = '';
    $("#dialog").hide();
    var dialog = function(shareLink) {
        $("#dialog").children(":input")[0].value = window.location.origin + shareLink;
        $("#dialog").dialog({ width: 350 });
    };

    // close the save dialogue
    $(function() {
        $( "input[name=Ok]" )
        .button()
        .click(function( event ) {
            event.preventDefault();
            $("#dialog").dialog("close");
        })
    });
