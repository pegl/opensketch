function getParameterInt(param) {
            var val = document.URL;
            var url = val.substr(val.indexOf(param))  
            var n=parseInt(url.replace(param+"=",""));
            return n; 
}

/*THIS FUNCTION IS TO FETCH STRING PARAMETER*/
function getParameter(param) {
            var val = document.URL;
            var url = val.substr(val.indexOf(param))  
            var n=url.replace(param+"=","");
            return n; 
}
